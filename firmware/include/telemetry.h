#pragma once

#include <stddef.h>

namespace weather_balloon {
namespace telemetry {

// Stub boundary for the existing LightAPRS GPS/radio firmware integration.
// Returns a deterministic safe sample until real flight data is wired in.
bool format_sample(char* output, size_t capacity);

}  // namespace telemetry
}  // namespace weather_balloon
