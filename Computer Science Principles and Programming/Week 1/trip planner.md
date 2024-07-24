# Trip planner

## Main Function: Trip Planner

- Name -> Trip planner
- Inputs -> Name of the destinations (Chennai, Pondicherry, Mahabalipuram, Kanyakumari, Trivendra) + Budget Planner + Crew + Road Trip Planner + Schedule maker + Accomodation booking
- Process -> Gathering and confirming the crew
  - Allocate initial budget using budget planner function
  - Preparing a schedule using schedule maker
  - Plan the destinations to visit according to schedule using road trip planner
  - Meanwhile if there are any expenses, allocate the respective expenses using budget planner
- Output ->  schedule, destinations to visit, Expenses of each member

## Function: Budget Planner

- Name -> Budget planner
- Inputs -> Name of the crew + Expenses + Description
- Process -> Divinding the expenses among the crew equally
- Output -> Name of each member and their respective debt for every other member.

## Road Trip Planner

- Name -> Road Trip planner
- Inputs -> Start + Destination
- Process -> Finds the shortest and fastest route from the start to destination.
- Output -> Gives the route to travel from the start to destination, Time taken to travel

## Schedule maker

- Name -> Schedule maker
- Input -> Start time + Road Trip Planner + time taken to visit each destination
- Process -> Allocates and plans schedule depending on the time taken to visit a destination and making a tour
- Output -> Calendar output

## Function: Accomodation booking

- Name -> Accomation maker
- Input -> Name of the hotel + Number of rooms + Number of days + Crew
- Process -> Calculates the expenses for number to days to stay in a hotel for the number of rooms
- Output -> Expenses
