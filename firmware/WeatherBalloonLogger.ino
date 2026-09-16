#include "include/cutdown.h"
#include "include/openlog.h"
#include "include/pins.h"
#include "include/telemetry.h"

namespace {
bool sample_written = false;
}

void setup() {
  // Safety invariant: cutdown is driven OFF before UART or application work.
  weather_balloon::cutdown::init_safe();

  if (!weather_balloon::openlog::init(weather_balloon::pins::kOpenLogBaud)) {
    return;
  }

  char record[48];
  if (weather_balloon::telemetry::format_sample(record, sizeof(record))) {
    weather_balloon::openlog::write_line("sequence,gps_fix,altitude_m,cutdown");
    weather_balloon::openlog::write_line(record);
    sample_written = true;
  }
}

void loop() {
  // The scaffold writes exactly one deterministic record. Production firmware
  // will schedule samples here; cutdown remains inactive unless explicit flight
  // policy calls set_active(true).
  if (sample_written) {
    __WFI();
  }
}
