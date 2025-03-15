from collections import deques


class Airport:
    def __init__(self):
        self.landing_queue = deque()  # Landing requests (normal and emergency)
        self.takeoff_queue = deque()  # Takeoff requests

    def request_landing(self, plane_id, emergency=False):
        if emergency:
            # Emergency landing, add to the front of the landing queue
            self.landing_queue.appendleft(plane_id)
        else:
            # Regular landing, add to the end of the landing queue
            self.landing_queue.append(plane_id)

    def request_takeoff(self, plane_id):
        self.takeoff_queue.append(plane_id)

    def land_plane(self):
        if self.landing_queue:
            plane = self.landing_queue.popleft()  # Land the first plane in the queue
            print(f"Plane {plane} has landed.")
        else:
            print("No planes waiting to land.")

    def takeoff_plane(self):
        if not self.landing_queue:  # Takeoffs are only allowed if no planes are waiting to land
            if self.takeoff_queue:
                plane = self.takeoff_queue.popleft()  # Takeoff the first plane in the takeoff queue
                print(f"Plane {plane} has taken off.")
            else:
                print("No planes waiting to take off.")
        else:
            print("Cannot take off, landing queue is not empty.")

    def emergency_landing(self, plane_id):
        self.request_landing(plane_id, emergency=True)
        print(f"Emergency landing for plane {plane_id}.")


# Example usage:
airport = Airport()

# Planes requesting landing
airport.request_landing("PlaneA")
airport.request_landing("PlaneB")

# Request for takeoff
airport.request_takeoff("Plane1")

# Emergency landing
airport.emergency_landing("PlaneC")

# Land a plane
airport.land_plane()

# Try taking off when landing queue is not empty
airport.takeoff_plane()

# Land another plane
airport.land_plane()

# Takeoff a plane now that landing queue is empty
airport.takeoff_plane()
