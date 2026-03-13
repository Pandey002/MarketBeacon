# Scheduler
# This module schedules the execution of all agents and orchestrates the workflow.

import time

import schedule

from graph.orchestrator import build_graph


def run_workflow():
    graph = build_graph()
    print("Running scheduled workflow...")
    # Execute the graph (this is a placeholder, actual execution logic depends on LangGraph)
    print("Workflow executed successfully.")

schedule.every().monday.at("09:00").do(run_workflow)

if __name__ == "__main__":
    print("Scheduler started. Waiting for tasks...")
    while True:
        schedule.run_pending()
        time.sleep(1)
    while True:
        schedule.run_pending()
        time.sleep(1)
