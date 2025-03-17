import random
import queue
import time


# Define a Plane class for easy tracking of plane type and ID
class Plane:
    def __init__(self, plane_id, request_type, is_emergency=False):
        self.plane_id = plane_id
        self.request_type = request_type
        self.is_emergency = is_emergency

    def __repr__(self):
        return f"Plane({self.plane_id}, {self.request_type}, Emergency={self.is_emergency})"


# Queue for landing requests (priority queue)
landing_queue = queue.PriorityQueue()
# Queue for takeoff requests (FIFO queue)
takeoff_queue = queue.Queue()


# Simulation functions
def add_landing_request(plane):
    # If emergency, assign highest priority (priority queue logic: -1 for emergency)
    if plane.is_emergency:
        landing_queue.put((0, plane))  # Emergency will have the highest priority (lowest number)
    else:
        landing_queue.put((1, plane))


def add_takeoff_request(plane):
    takeoff_queue.put(plane)


def process_landing():
    if not landing_queue.empty():
        # Get the highest priority plane (lowest priority number)
        _, plane = landing_queue.get()
        print(f"Plane {plane.plane_id} is landing.")
    else:
        print("No planes waiting for landing.")


def process_takeoff():
    if landing_queue.empty() and not takeoff_queue.empty():
        plane = takeoff_queue.get()
        print(f"Plane {plane.plane_id} is taking off.")
    else:
        print("Takeoff denied: Landing queue is not empty or no planes waiting to take off.")


def simulate():
    plane_id = 1
    for _ in range(10):  # Run the simulation for 10 steps
        action = random.choice(['landing', 'takeoff'])
        emergency = random.choice([True, False]) if action == 'landing' else False

        if action == 'landing':
            print(f"Request: Plane {plane_id} requesting landing. Emergency: {emergency}")
            add_landing_request(Plane(plane_id, 'landing', emergency))
        elif action == 'takeoff':
            print(f"Request: Plane {plane_id} requesting takeoff.")
            add_takeoff_request(Plane(plane_id, 'takeoff'))

        # Process the queues
        process_landing()
        process_takeoff()

        plane_id += 1
        time.sleep(1)


# Run the simulation
simulate()
