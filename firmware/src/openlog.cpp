#include "../include/openlog.h"

#include <Arduino.h>
#include <sam.h>

#include "../include/pins.h"

namespace weather_balloon {
namespace openlog {
namespace {
bool initialized = false;

void write_byte(char value) {
  if (!initialized) {
    return;
  }
  while (!SERCOM4->USART.INTFLAG.bit.DRE) {
  }
  SERCOM4->USART.DATA.reg = static_cast<uint16_t>(static_cast<uint8_t>(value));
}
}

bool init(uint32_t baud) {
  if (baud == 0 || SystemCoreClock == 0) {
    return false;
  }

  // Arduino SAMD establishes GCLK0/SystemCoreClock. Enable only the documented
  // SERCOM4 core; GPS Serial1 and occupied radio buses are untouched.
  PM->APBCMASK.reg |= PM_APBCMASK_SERCOM4;
  GCLK->CLKCTRL.reg = GCLK_CLKCTRL_ID(GCM_SERCOM4_CORE) |
                      GCLK_CLKCTRL_GEN_GCLK0 | GCLK_CLKCTRL_CLKEN;
  while (GCLK->STATUS.bit.SYNCBUSY) {
  }

  SERCOM4->USART.CTRLA.bit.SWRST = 1;
  while (SERCOM4->USART.CTRLA.bit.SWRST || SERCOM4->USART.STATUS.bit.SYNCBUSY) {
  }

  // PB08 function D is SERCOM4/PAD0. Enable TX only: no RX pin is claimed.
  auto& port = PORT->Group[pins::kOpenLogTxPortGroup];
  port.PINCFG[pins::kOpenLogTxPortPin].bit.PMUXEN = 1;
  auto& pmux = port.PMUX[pins::kOpenLogTxPortPin / 2];
  pmux.reg = static_cast<uint8_t>((pmux.reg & PORT_PMUX_PMUXO_Msk) | PORT_PMUX_PMUXE_D);

  const uint64_t scaled = 65536ULL * 16ULL * baud;
  if (scaled >= 65536ULL * SystemCoreClock) {
    return false;
  }
  SERCOM4->USART.BAUD.reg = static_cast<uint16_t>(65536ULL - scaled / SystemCoreClock);
  SERCOM4->USART.CTRLA.reg = SERCOM_USART_CTRLA_MODE_USART_INT_CLK |
                            SERCOM_USART_CTRLA_DORD |
                            SERCOM_USART_CTRLA_TXPO(0) |
                            SERCOM_USART_CTRLA_RXPO(1);
  SERCOM4->USART.CTRLB.reg = SERCOM_USART_CTRLB_TXEN;
  while (SERCOM4->USART.STATUS.bit.SYNCBUSY) {
  }
  SERCOM4->USART.CTRLA.bit.ENABLE = 1;
  while (SERCOM4->USART.STATUS.bit.SYNCBUSY) {
  }
  initialized = true;
  return true;
}

void write(const char* text) {
  if (text == nullptr) {
    return;
  }
  while (*text != '\0') {
    write_byte(*text++);
  }
}

void write_line(const char* text) {
  write(text);
  write_byte('\r');
  write_byte('\n');
  flush();
}

void flush() {
  if (!initialized) {
    return;
  }
  while (!SERCOM4->USART.INTFLAG.bit.TXC) {
  }
}

}  // namespace openlog
}  // namespace weather_balloon
