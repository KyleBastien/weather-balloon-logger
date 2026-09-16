#pragma once

namespace weather_balloon {
namespace cutdown {

// Must be the first application-level initialization call. Drives A2/PB09 low.
void init_safe();

// Driver scaffold. Flight policy must enforce arming, timeout, and one-shot use.
void set_active(bool active);

bool is_active();

}  // namespace cutdown
}  // namespace weather_balloon
