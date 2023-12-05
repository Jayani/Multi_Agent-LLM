# Main
from AutonomousElectricVehicle import Vehicle
from LocalNavigationAgent import LocalNavigationAgent
from CentralizedControlAgent import CentralizedControlAgent
from CommunicationAgent import CommunicationAgent
from EnergyManagementAgent import EnergyManagementAgent
from EnergyManagementAgent import ChargingStation
from SafetyMonitoringAgent import SafetyMonitoringAgent
from MaintenanceAgent import MaintenanceAgent
from HelpDeskAgent import HelpDeskAgent
from UserAgent import UserAgent

# Create instances of AEVs with associated agents
ae1 = Vehicle(vehicle_id=1)
ae2 = Vehicle(vehicle_id=2)

# Test CentralizedControlAgent
#===================================================================================================================
centralizedControl_agent = CentralizedControlAgent([ae1, ae2],"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")
centralizedControl_agent.plan_route_for_vehicle(ae1, "London","shortest path")
centralizedControl_agent.allocate_resources()

# Test LocalNavigationAgent
#==================================================================================================================
localNavigation_agent = LocalNavigationAgent(ae1, "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")

# Set initial vehicle location and destination
ae1.update_location("Oxford")
ae1.update_destination("Wembley")
localNavigation_agent.navigate()

# Test CommunicationAgent
#============================================================================================================
communication_agent1 = CommunicationAgent(ae1, "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")
communication_agent2 = CommunicationAgent(ae2, "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")

# Update neighbors for communication
communication_agent1.update_neighbors([ae1])
communication_agent2.update_neighbors([ae2])

# Share traffic information between vehicles
communication_agent1.share_traffic_info()
communication_agent2.share_traffic_info()

# Test EnergyManagementAgent
#====================================================================================================================
charging_station1 = ChargingStation(station_id=1)
charging_station2 = ChargingStation(station_id=2)

energy_agent1 = EnergyManagementAgent(ae1, [charging_station1, charging_station2], "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")

# Perform energy management tasks
energy_agent1.optimize_charging_schedule()

# Test SafetyMonitoringAgent
#=======================================================================================================================
safetyMonitoring_agent = SafetyMonitoringAgent(ae1, "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")
safetyMonitoring_agent.monitor_safety()

# Test MaintenanceAgent
#========================================================================================================================
maintenance_agent = MaintenanceAgent(ae1, "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")
maintenance_agent.monitor_vehicle_health()
maintenance_agent.schedule_maintenance()

# Test HelpDeskAgent
#==================================================================================================================
helpdesk_agent = HelpDeskAgent("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")
helpdesk_agent.handle_user_query(ae1, "What is the charging status of my vehicle?")

# Test UserAgent
#===================================================================================================================
user_agent = UserAgent(1, "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")
user_agent.request_ride("Oxford","London")
user_agent.ask_question("How can I optimize my route?")
