"""
Travel Manager Portmanteau

Comprehensive travel planning and transport management including:
- Public transport schedules (Wiener Linien integration)
- Travel planning and itinerary creation
- Weather and travel conditions
- Currency exchange and visa information
- Sleeper train schedules and booking

This portmanteau integrates with external APIs for real-time transport data.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def register_travel_tools(app):
    """Register all travel manager tools with the MCP server."""

    @app.tool()
    async def get_next_tram(
        station_name: str,
        line: Optional[str] = None,
        direction: Optional[str] = None,
        limit: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Get next tram/bus/metro departures from a station.

        Args:
            station_name: Name of the station/stop
            line: Specific line number (optional)
            direction: Travel direction (optional)
            limit: Maximum departures to return (default: 3)

        Returns:
            List of upcoming departures with real-time data
        """
        try:
            # TODO: Integrate with Wiener Linien API
            # For now, return mock data
            mock_departures = [
                {
                    "line": line or "U6",
                    "direction": direction or "Floridsdorf",
                    "departure_time": (datetime.now() + timedelta(minutes=2)).strftime("%H:%M"),
                    "minutes_until": 2,
                    "platform": "A",
                    "delay_minutes": 0,
                    "is_realtime": True
                },
                {
                    "line": line or "U6",
                    "direction": direction or "Floridsdorf",
                    "departure_time": (datetime.now() + timedelta(minutes=7)).strftime("%H:%M"),
                    "minutes_until": 7,
                    "platform": "A",
                    "delay_minutes": 0,
                    "is_realtime": True
                },
                {
                    "line": line or "U6",
                    "direction": direction or "Floridsdorf",
                    "departure_time": (datetime.now() + timedelta(minutes=12)).strftime("%H:%M"),
                    "minutes_until": 12,
                    "platform": "A",
                    "delay_minutes": 0,
                    "is_realtime": True
                }
            ]

            departures = mock_departures[:limit]
            logger.info(f"Retrieved {len(departures)} departures from {station_name}")
            return departures

        except Exception as e:
            logger.error(f"Failed to get departures from {station_name}: {e}")
            return []

    @app.tool()
    async def get_transport_schedule(
        line_number: str,
        station_name: str,
        date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get complete schedule for a transport line at a station.

        Args:
            line_number: Transport line (e.g., "U6", "1", "74A")
            station_name: Station name
            date: Date for schedule (default: today)

        Returns:
            Complete schedule for the day
        """
        try:
            schedule_date = date or datetime.now().strftime("%Y-%m-%d")

            # TODO: Integrate with Wiener Linien API
            mock_schedule = {
                "line": line_number,
                "station": station_name,
                "date": schedule_date,
                "direction_1": "Floridsdorf",
                "direction_2": "Siebenhirten",
                "departures": [
                    {"time": "05:30", "direction": "Floridsdorf"},
                    {"time": "05:45", "direction": "Floridsdorf"},
                    {"time": "06:00", "direction": "Floridsdorf"},
                    {"time": "06:15", "direction": "Floridsdorf"},
                    # ... more departures
                    {"time": "23:30", "direction": "Floridsdorf"},
                ],
                "frequency": "Every 5 minutes (peak), Every 7-8 minutes (off-peak)",
                "last_updated": datetime.now().isoformat()
            }

            logger.info(f"Retrieved schedule for {line_number} at {station_name}")
            return mock_schedule

        except Exception as e:
            logger.error(f"Failed to get schedule for {line_number} at {station_name}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_transport_disruptions(
        line: Optional[str] = None,
        area: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get current transport disruptions and delays.

        Args:
            line: Specific line to check (optional)
            area: Geographic area to check (optional)

        Returns:
            Current disruptions with details and alternatives
        """
        try:
            # TODO: Integrate with Wiener Linien disruptions API
            mock_disruptions = [
                {
                    "line": "U1",
                    "type": "Delay",
                    "description": "Signal failure at Karlsplatz",
                    "delay_minutes": 5,
                    "affected_stations": ["Karlsplatz", "Stephansplatz", "Schwedenplatz"],
                    "start_time": "08:30",
                    "estimated_end": "09:15",
                    "alternative_routes": ["Use U4 from Karlsplatz to Schwedenplatz"]
                },
                {
                    "line": "74A",
                    "type": "Detour",
                    "description": "Road construction on Favoritenstraße",
                    "delay_minutes": 10,
                    "affected_stations": ["Favoritenstraße", "Gudrunstraße"],
                    "start_time": "07:00",
                    "estimated_end": "18:00",
                    "alternative_routes": ["Use 6 tram to reach destination"]
                }
            ]

            # Filter by line if specified
            if line:
                mock_disruptions = [d for d in mock_disruptions if d["line"] == line]

            logger.info(f"Retrieved {len(mock_disruptions)} transport disruptions")
            return mock_disruptions

        except Exception as e:
            logger.error(f"Failed to get transport disruptions: {e}")
            return []

    @app.tool()
    async def plan_day_trip(
        destination: str,
        departure_time: Optional[str] = None,
        return_time: Optional[str] = None,
        budget: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Plan a complete day trip itinerary.

        Args:
            destination: Trip destination
            departure_time: Preferred departure time (default: 08:00)
            return_time: Preferred return time (default: 20:00)
            budget: Budget limit for the trip (optional)

        Returns:
            Complete day trip itinerary with transport and activities
        """
        try:
            dep_time = departure_time or "08:00"
            ret_time = return_time or "20:00"

            # TODO: Implement intelligent trip planning with real data
            mock_itinerary = {
                "destination": destination,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "departure_time": dep_time,
                "return_time": ret_time,
                "transport": {
                    "outbound": {
                        "type": "Train",
                        "line": "R95",
                        "departure": f"{dep_time} from Wien Hauptbahnhof",
                        "arrival": f"{(datetime.strptime(dep_time, '%H:%M') + timedelta(hours=1, minutes=30)).strftime('%H:%M')} at {destination}",
                        "cost": 15.50
                    },
                    "return": {
                        "type": "Train",
                        "line": "R95",
                        "departure": f"{ret_time} from {destination}",
                        "arrival": f"{(datetime.strptime(ret_time, '%H:%M') + timedelta(hours=1, minutes=30)).strftime('%H:%M')} at Wien Hauptbahnhof",
                        "cost": 15.50
                    }
                },
                "activities": [
                    {
                        "time": "10:30-12:00",
                        "activity": "Visit main attraction",
                        "cost": 12.00,
                        "notes": "Book tickets in advance"
                    },
                    {
                        "time": "12:00-13:30",
                        "activity": "Lunch at local restaurant",
                        "cost": 25.00,
                        "notes": "Try local specialties"
                    },
                    {
                        "time": "14:00-16:00",
                        "activity": "Explore old town",
                        "cost": 0.00,
                        "notes": "Walking tour recommended"
                    }
                ],
                "costs": {
                    "transport": 31.00,
                    "activities": 37.00,
                    "food_drink": 35.00,
                    "misc": 10.00,
                    "total": 113.00
                },
                "budget_check": "Within budget" if budget is None or 113.00 <= budget else f"Over budget by €{113.00 - budget}",
                "tips": [
                    "Check weather forecast before departure",
                    "Download offline maps",
                    "Bring comfortable walking shoes",
                    "Check for local events or festivals"
                ]
            }

            logger.info(f"Generated day trip plan for {destination}")
            return mock_itinerary

        except Exception as e:
            logger.error(f"Failed to plan day trip to {destination}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_travel_info(
        city_name: str,
        info_type: str = "transport"
    ) -> Dict[str, Any]:
        """
        Get comprehensive travel information for a city.

        Args:
            city_name: Name of the destination city
            info_type: Type of information ("transport", "attractions", "accommodation", "costs")

        Returns:
            Detailed travel information based on type
        """
        try:
            # TODO: Integrate with travel APIs and knowledge base
            mock_info = {
                "city": city_name,
                "country": "Austria",  # Would be determined based on city
                "info_type": info_type,
                "last_updated": datetime.now().isoformat()
            }

            if info_type == "transport":
                mock_info["transport"] = {
                    "from_vienna": {
                        "train": {"duration": "2h 30min", "cost": "€25-45", "frequency": "Every 30-60 min"},
                        "bus": {"duration": "3-4 hours", "cost": "€15-25", "frequency": "Several daily"},
                        "car": {"duration": "2-3 hours", "cost": "Toll + fuel ~€15", "parking": "€5-10/day"}
                    },
                    "local_transport": {
                        "cost": "€2.40/single ride",
                        "day_pass": "€5.80",
                        "week_pass": "€17.10"
                    }
                }
            elif info_type == "attractions":
                mock_info["attractions"] = [
                    {"name": "Old Town", "cost": "Free", "time_needed": "2-3 hours"},
                    {"name": "Main Castle", "cost": "€15", "time_needed": "1-2 hours"},
                    {"name": "Museum Quarter", "cost": "€12-18", "time_needed": "2-4 hours"}
                ]
            elif info_type == "accommodation":
                mock_info["accommodation"] = {
                    "budget": {"cost_per_night": "€40-70", "type": "Hostel/Guesthouse"},
                    "mid_range": {"cost_per_night": "€70-120", "type": "3-star hotel"},
                    "luxury": {"cost_per_night": "€150+", "type": "4-5 star hotel"}
                }
            elif info_type == "costs":
                mock_info["costs"] = {
                    "meal_budget": "€15-25",
                    "meal_mid_range": "€25-45",
                    "beer_local": "€3-4",
                    "coffee": "€2-3.50",
                    "daily_cost_estimate": "€50-100 per person"
                }

            logger.info(f"Retrieved {info_type} information for {city_name}")
            return mock_info

        except Exception as e:
            logger.error(f"Failed to get travel info for {city_name}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_weather_for_travel(location: str, days_ahead: int = 3) -> List[Dict[str, Any]]:
        """
        Get weather forecast optimized for travel planning.

        Args:
            location: Location name
            days_ahead: Number of days to forecast (default: 3)

        Returns:
            Weather forecast with travel-relevant information
        """
        try:
            # TODO: Integrate with weather API
            mock_weather = []
            base_date = datetime.now()

            for i in range(min(days_ahead, 7)):  # Max 7 days
                forecast_date = base_date + timedelta(days=i)
                mock_weather.append({
                    "date": forecast_date.strftime("%Y-%m-%d"),
                    "day": forecast_date.strftime("%A"),
                    "temperature_max": 15 + i,  # Mock increasing temps
                    "temperature_min": 5 + i,
                    "precipitation_chance": 20 + (i * 10),  # Increasing chance
                    "precipitation_amount": f"{i * 2}mm",
                    "wind_speed": 10 + i,
                    "conditions": ["Sunny", "Partly Cloudy", "Cloudy", "Light Rain"][i % 4],
                    "travel_advice": "Good weather for outdoor activities" if i < 2 else "Check weather before outdoor plans",
                    "clothing_advice": "Light jacket recommended" if i < 3 else "Bring umbrella and waterproof jacket"
                })

            logger.info(f"Retrieved {len(mock_weather)}-day weather forecast for {location}")
            return mock_weather

        except Exception as e:
            logger.error(f"Failed to get weather for {location}: {e}")
            return []

    @app.tool()
    async def get_train_schedule(
        from_station: str,
        to_station: str,
        date: Optional[str] = None,
        time: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get ÖBB train schedules between stations.

        Args:
            from_station: Departure station
            to_station: Arrival station
            date: Travel date (default: today)
            time: Earliest departure time (default: now)

        Returns:
            Available train connections with details
        """
        try:
            # TODO: Integrate with ÖBB API
            mock_trains = [
                {
                    "type": "Railjet",
                    "departure": {
                        "station": from_station,
                        "time": "08:30",
                        "platform": "3"
                    },
                    "arrival": {
                        "station": to_station,
                        "time": "10:45",
                        "platform": "2"
                    },
                    "duration": "2h 15min",
                    "changes": 0,
                    "price": 42.50,
                    "class": "Economy",
                    "amenities": ["WiFi", "Power outlets", "Restaurant"]
                },
                {
                    "type": "Regional Express",
                    "departure": {
                        "station": from_station,
                        "time": "09:15",
                        "station": from_station,
                        "time": "09:15",
                        "platform": "7"
                    },
                    "arrival": {
                        "station": to_station,
                        "time": "11:42",
                        "platform": "1"
                    },
                    "duration": "2h 27min",
                    "changes": 1,
                    "price": 28.90,
                    "class": "Economy",
                    "amenities": ["WiFi"]
                }
            ]

            logger.info(f"Retrieved {len(mock_trains)} train connections from {from_station} to {to_station}")
            return mock_trains

        except Exception as e:
            logger.error(f"Failed to get train schedule from {from_station} to {to_station}: {e}")
            return []

    @app.tool()
    async def get_bus_schedule(
        from_city: str,
        to_city: str,
        date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get long-distance bus schedules.

        Args:
            from_city: Departure city
            to_city: Arrival city
            date: Travel date (default: today)

        Returns:
            Available bus connections
        """
        try:
            # TODO: Integrate with bus company APIs (FlixBus, RegioJet, etc.)
            mock_buses = [
                {
                    "company": "FlixBus",
                    "departure": {
                        "city": from_city,
                        "station": f"{from_city} Central Station",
                        "time": "22:00"
                    },
                    "arrival": {
                        "city": to_city,
                        "station": f"{to_city} Central Station",
                        "time": "05:30"
                    },
                    "duration": "7h 30min",
                    "price": 19.99,
                    "amenities": ["WiFi", "Power outlets", "Toilet"],
                    "overnight": True
                },
                {
                    "company": "RegioJet",
                    "departure": {
                        "city": from_city,
                        "station": f"{from_city} Main Station",
                        "time": "14:30"
                    },
                    "arrival": {
                        "city": to_city,
                        "station": f"{to_city} Main Station",
                        "time": "19:45"
                    },
                    "duration": "5h 15min",
                    "price": 24.50,
                    "amenities": ["WiFi", "Snacks", "Entertainment"],
                    "overnight": False
                }
            ]

            logger.info(f"Retrieved {len(mock_buses)} bus connections from {from_city} to {to_city}")
            return mock_buses

        except Exception as e:
            logger.error(f"Failed to get bus schedule from {from_city} to {to_city}: {e}")
            return []

    @app.tool()
    async def get_flight_info(
        from_airport: str,
        to_airport: str,
        date: Optional[str] = None,
        flexible_dates: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Get flight information (when implementing, integrate with flight APIs).

        Args:
            from_airport: Departure airport code
            to_airport: Arrival airport code
            date: Flight date
            flexible_dates: Search flexible dates +/- 3 days

        Returns:
            Available flights with details
        """
        try:
            # TODO: Integrate with flight APIs (Amadeus, Skyscanner, etc.)
            mock_flights = [
                {
                    "airline": "Austrian Airlines",
                    "flight_number": "OS891",
                    "departure": {
                        "airport": from_airport,
                        "time": "06:25",
                        "terminal": "T1"
                    },
                    "arrival": {
                        "airport": to_airport,
                        "time": "07:40",
                        "terminal": "T2"
                    },
                    "duration": "1h 15min",
                    "price": 89.99,
                    "class": "Economy",
                    "stops": 0,
                    "aircraft": "Embraer 195"
                },
                {
                    "airline": "Lufthansa",
                    "flight_number": "LH1234",
                    "departure": {
                        "airport": from_airport,
                        "time": "14:20",
                        "terminal": "T1"
                    },
                    "arrival": {
                        "airport": to_airport,
                        "time": "15:35",
                        "terminal": "T2"
                    },
                    "duration": "1h 15min",
                    "price": 124.50,
                    "class": "Economy",
                    "stops": 0,
                    "aircraft": "Airbus A320"
                }
            ]

            logger.info(f"Retrieved {len(mock_flights)} flights from {from_airport} to {to_airport}")
            return mock_flights

        except Exception as e:
            logger.error(f"Failed to get flight info from {from_airport} to {to_airport}: {e}")
            return []

    @app.tool()
    async def get_currency_exchange(
        from_currency: str = "EUR",
        to_currency: str = "USD",
        amount: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Get current currency exchange rates.

        Args:
            from_currency: Source currency code (default: EUR)
            to_currency: Target currency code (default: USD)
            amount: Amount to convert (optional)

        Returns:
            Exchange rate and converted amount
        """
        try:
            # TODO: Integrate with currency API (e.g., fixer.io, exchangerate-api.com)
            mock_rates = {
                "EUR": {"USD": 1.0847, "GBP": 0.8523, "CHF": 0.9372},
                "USD": {"EUR": 0.9221, "GBP": 0.7859, "CHF": 0.8637},
                "GBP": {"EUR": 1.1732, "USD": 1.2723, "CHF": 1.0987}
            }

            if from_currency not in mock_rates or to_currency not in mock_rates[from_currency]:
                return {"error": f"Exchange rate not available for {from_currency} to {to_currency}"}

            rate = mock_rates[from_currency][to_currency]
            converted_amount = amount * rate if amount else None

            result = {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "exchange_rate": rate,
                "last_updated": datetime.now().isoformat(),
                "source": "European Central Bank"  # Mock source
            }

            if converted_amount is not None:
                result["original_amount"] = amount
                result["converted_amount"] = round(converted_amount, 2)

            logger.info(f"Retrieved exchange rate {from_currency} to {to_currency}: {rate}")
            return result

        except Exception as e:
            logger.error(f"Failed to get currency exchange for {from_currency} to {to_currency}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_visa_requirements(citizenship: str, destination_country: str) -> Dict[str, Any]:
        """
        Get visa information for destinations.

        Args:
            citizenship: Passport country
            destination_country: Travel destination

        Returns:
            Visa requirements and application details
        """
        try:
            # TODO: Integrate with official government APIs or visa services
            mock_visa_info = {
                "citizenship": citizenship,
                "destination": destination_country,
                "visa_required": False,  # For EU/Schengen countries
                "max_stay": "90 days in 180-day period",
                "notes": "As EU/Schengen citizen, no visa required for stays up to 90 days",
                "last_updated": datetime.now().isoformat()
            }

            # Add specific requirements for non-EU destinations
            if destination_country.lower() not in ["austria", "germany", "france", "italy", "spain"]:
                mock_visa_info.update({
                    "visa_required": True,
                    "visa_type": "Tourist Visa",
                    "processing_time": "2-4 weeks",
                    "cost": "€60-120",
                    "application_url": f"https://www.{destination_country.lower()}-embassy.at",
                    "requirements": [
                        "Valid passport (6+ months validity)",
                        "Application form",
                        "Recent passport photo",
                        "Flight itinerary",
                        "Hotel booking confirmation",
                        "Bank statements",
                        "Employment letter"
                    ]
                })

            logger.info(f"Retrieved visa requirements for {citizenship} citizen traveling to {destination_country}")
            return mock_visa_info

        except Exception as e:
            logger.error(f"Failed to get visa requirements for {citizenship} to {destination_country}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def calculate_travel_cost(
        transport_cost: float,
        accommodation_cost: Optional[float] = None,
        food_cost: Optional[float] = None,
        activities_cost: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculate total travel costs with breakdown.

        Args:
            transport_cost: Cost of transportation
            accommodation_cost: Cost of accommodation (optional)
            food_cost: Cost of food/dining (optional)
            activities_cost: Cost of activities/attractions (optional)

        Returns:
            Total cost breakdown and budget analysis
        """
        try:
            costs = {
                "transport": transport_cost,
                "accommodation": accommodation_cost or 0,
                "food": food_cost or 0,
                "activities": activities_cost or 0
            }

            total_cost = sum(costs.values())
            per_person_cost = total_cost  # Assuming single traveler

            # Add estimates for unspecified costs
            estimates = {}
            if not accommodation_cost:
                estimates["accommodation_estimate"] = total_cost * 0.4  # Assume 40% of budget
            if not food_cost:
                estimates["food_estimate"] = total_cost * 0.3  # Assume 30% of budget
            if not activities_cost:
                estimates["activities_estimate"] = total_cost * 0.2  # Assume 20% of budget

            result = {
                "cost_breakdown": costs,
                "total_cost": total_cost,
                "per_person_cost": per_person_cost,
                "estimates": estimates,
                "budget_categories": {
                    "low_budget": total_cost * 0.7,      # 30% savings
                    "comfortable": total_cost,            # Break even
                    "luxury": total_cost * 1.5           # 50% extra
                },
                "tips": [
                    "Add 10-15% buffer for unexpected expenses",
                    "Consider travel insurance (5-10% of total cost)",
                    "Check for discounts with travel cards/clubs"
                ]
            }

            logger.info(f"Calculated travel cost breakdown: €{total_cost}")
            return result

        except Exception as e:
            logger.error(f"Failed to calculate travel cost: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_sleeper_train_schedule(
        from_city: str,
        to_city: str,
        date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get ÖBB Nightjet sleeper train schedules.

        Args:
            from_city: Departure city
            to_city: Arrival city
            date: Travel date (default: today)

        Returns:
            Available sleeper train connections
        """
        try:
            # TODO: Integrate with ÖBB Nightjet API
            mock_sleeper_trains = [
                {
                    "route": f"{from_city} → {to_city}",
                    "train_type": "Nightjet",
                    "departure": {
                        "city": from_city,
                        "station": f"{from_city} Hauptbahnhof",
                        "time": "22:40",
                        "platform": "12"
                    },
                    "arrival": {
                        "city": to_city,
                        "station": f"{to_city} Centrale",
                        "time": "05:40",
                        "platform": "5"
                    },
                    "duration": "7h 00min",
                    "distance": "490 km",
                    "sleeping_car_options": [
                        {"type": "Comfort", "price": 89.00, "beds": 1, "facilities": ["Washbasin", "Towel", "Breakfast"]},
                        {"type": "Deluxe", "price": 129.00, "beds": 1, "facilities": ["Private shower", "Towels", "Breakfast", "Newspaper"]},
                        {"type": "Suite", "price": 159.00, "beds": 2, "facilities": ["Private shower/toilet", "Towels", "Breakfast", "Newspaper", "Welcome drink"]}
                    ],
                    "couchette_options": [
                        {"type": "6-bed", "price": 49.00, "facilities": ["Reading light", "Lockers"]},
                        {"type": "4-bed", "price": 69.00, "facilities": ["Reading light", "Lockers", "Power outlets"]}
                    ],
                    "amenities": ["Restaurant car", "WiFi", "Power outlets", "Luggage storage"],
                    "route_highlights": ["Alpine scenery", "Dolomites views", "Italian countryside"],
                    "booking_url": "https://www.oebb.at/en/tickets-travelling/nightjets"
                }
            ]

            logger.info(f"Retrieved {len(mock_sleeper_trains)} sleeper train connections from {from_city} to {to_city}")
            return mock_sleeper_trains

        except Exception as e:
            logger.error(f"Failed to get sleeper train schedule from {from_city} to {to_city}: {e}")
            return []

    @app.tool()
    async def get_traffic_info(
        route_from: str,
        route_to: str,
        transport_mode: str = "car"
    ) -> Dict[str, Any]:
        """
        Get real-time traffic information.

        Args:
            route_from: Starting location
            route_to: Destination location
            transport_mode: Transport type ("car", "public", "bike")

        Returns:
            Current traffic conditions and estimated travel times
        """
        try:
            # TODO: Integrate with traffic APIs (Google Maps, HERE, TomTom)
            mock_traffic = {
                "route": f"{route_from} to {route_to}",
                "transport_mode": transport_mode,
                "current_conditions": {
                    "status": "Normal traffic",
                    "congestion_level": "Low (1/5)",
                    "average_speed": "85 km/h",
                    "free_flow_speed": "90 km/h"
                },
                "estimated_travel_time": {
                    "normal": "45 minutes",
                    "current": "52 minutes",
                    "delay": "7 minutes"
                },
                "incidents": [
                    {
                        "type": "Construction",
                        "location": "A1 Highway, km 15-18",
                        "description": "Road works, expect delays",
                        "delay": "5-10 minutes",
                        "end_date": "2025-12-20"
                    }
                ],
                "alternative_routes": [
                    {
                        "name": "Scenic Route",
                        "distance": "+5 km",
                        "time": "+12 minutes",
                        "reason": "Avoids highway construction"
                    }
                ],
                "last_updated": datetime.now().isoformat(),
                "source": "Austrian Traffic Information Service"
            }

            logger.info(f"Retrieved traffic information for route {route_from} to {route_to}")
            return mock_traffic

        except Exception as e:
            logger.error(f"Failed to get traffic info for route {route_from} to {route_to}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def book_transport_ticket(
        transport_type: str,
        from_location: str,
        to_location: str,
        date: str,
        passengers: int = 1
    ) -> Dict[str, Any]:
        """
        Book transport tickets (placeholder - would integrate with booking APIs).

        Args:
            transport_type: Type of transport ("train", "bus", "flight")
            from_location: Departure location
            to_location: Arrival location
            date: Travel date
            passengers: Number of passengers (default: 1)

        Returns:
            Booking confirmation or booking link
        """
        try:
            # TODO: Integrate with actual booking APIs (ÖBB, FlixBus, airline APIs)
            mock_booking = {
                "transport_type": transport_type,
                "route": f"{from_location} → {to_location}",
                "date": date,
                "passengers": passengers,
                "status": "Booking simulation",
                "booking_options": [
                    {
                        "provider": "ÖBB" if transport_type == "train" else "FlixBus",
                        "price_per_person": 42.50,
                        "total_price": 42.50 * passengers,
                        "departure_time": "08:30",
                        "arrival_time": "10:45",
                        "booking_url": f"https://www.oebb.at/en/tickets-travelling",
                        "conditions": "Flexible cancellation up to 24 hours before departure"
                    }
                ],
                "payment_methods": ["Credit Card", "PayPal", "Bank Transfer"],
                "cancellation_policy": "Free cancellation up to 24 hours before departure",
                "note": "This is a simulation. Actual booking would require integration with booking APIs."
            }

            logger.info(f"Generated booking options for {transport_type} from {from_location} to {to_location}")
            return mock_booking

        except Exception as e:
            logger.error(f"Failed to book {transport_type} ticket: {e}")
            return {"error": str(e)}

    logger.info("[OK] Travel Manager portmanteau tools registered")
