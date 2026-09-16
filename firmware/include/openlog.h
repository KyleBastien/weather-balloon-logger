#pragma once

#include <stdint.h>

namespace weather_balloon {
namespace openlog {

// Initializes polling, transmit-only SERCOM4 on PB08/PAD0.
bool init(uint32_t baud);
void write(const char* text);
void write_line(const char* text);
void flush();

}  // namespace openlog
}  // namespace weather_balloon
