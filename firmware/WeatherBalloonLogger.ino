#include "include/openlog.h"
#include "include/pins.h"
#include "include/telemetry.h"

namespace {
bool sample_written = false;
}

void setup() {
  // A2/PB09 is active-low. Preload HIGH before enabling the output so reset
  // and initialization cannot flash the activity LED.
  digitalWrite(weather_balloon::pins::kActivityLed, HIGH);
  pinMode(weather_balloon::pins::kActivityLed, OUTPUT);

  if (!weather_balloon::openlog::init(weather_balloon::pins::kOpenLogBaud)) {
    return;
  }

  char record[48];
  if (weather_balloon::telemetry::format_sample(record, sizeof(record))) {
    digitalWrite(weather_balloon::pins::kActivityLed, LOW);
    weather_balloon::openlog::write_line("sequence,gps_fix,altitude_m,logger");
    weather_balloon::openlog::write_line(record);
    digitalWrite(weather_balloon::pins::kActivityLed, HIGH);
    sample_written = true;
  }
}

void loop() {
  // The scaffold writes exactly one deterministic record. Production firmware
  // will schedule samples here. LightHAB's own upstream firmware retains sole
  // ownership of its OUT1 cutdown behavior.
  if (sample_written) {
    __WFI();
  }
}
