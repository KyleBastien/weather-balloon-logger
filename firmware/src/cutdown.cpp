#include "../include/cutdown.h"

#include <Arduino.h>

#include "../include/pins.h"

namespace weather_balloon {
namespace cutdown {
namespace {
bool active = false;
}

void init_safe() {
  // Set the output latch low before enabling the pin as an output. R3 also
  // holds Q1 off during reset, before firmware executes.
  digitalWrite(pins::kCutdownCtrl, LOW);
  pinMode(pins::kCutdownCtrl, OUTPUT);
  active = false;
}

void set_active(bool requested) {
  digitalWrite(pins::kCutdownCtrl, requested ? HIGH : LOW);
  active = requested;
}

bool is_active() { return active; }

}  // namespace cutdown
}  // namespace weather_balloon
