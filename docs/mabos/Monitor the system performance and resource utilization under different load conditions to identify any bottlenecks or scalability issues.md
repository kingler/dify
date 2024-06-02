To monitor system performance and resource utilization under different load conditions, follow these steps:

### Step 1: Understand the Requirements
1. **Performance Metrics**: Identify key performance metrics (e.g., response time, throughput, CPU, memory usage).
2. **Scalability**: Ensure the system can handle increasing load.
3. **Bottlenecks**: Identify and address performance bottlenecks.

### Step 2: Choose Monitoring Tools
- **Prometheus**: For metrics collection.
- **Grafana**: For visualization.
- **Apache JMeter**: For load testing.

### Step 3: Set Up Monitoring
1. **Install Prometheus and Grafana**: Follow official installation guides.
2. **Configure Prometheus**: Set up Prometheus to scrape metrics from your services.
3. **Create Grafana Dashboards**: Visualize metrics in Grafana.

### Step 4: Implement Metrics Collection
1. **Expose Metrics in API**:
   ```python:api/metrics.py
   from prometheus_client import start_http_server, Summary

   REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

   @REQUEST_TIME.time()
   def process_request():
       # Your request processing logic
       pass

   if __name__ == '__main__':
       start_http_server(8000)
       while True:
           process_request()
   ```

2. **Expose Metrics in MABOS**:
   ```python:mabos/metrics.py
   from prometheus_client import start_http_server, Summary

   TASK_PROCESSING_TIME = Summary('task_processing_seconds', 'Time spent processing task')

   @TASK_PROCESSING_TIME.time()
   def process_task():
       # Your task processing logic
       pass

   if __name__ == '__main__':
       start_http_server(8001)
       while True:
           process_task()
   ```

### Step 5: Load Testing
1. **Create JMeter Test Plan**: Simulate load and measure performance.
2. **Run Load Tests**: Execute tests and collect metrics.

### Step 6: Analyze and Optimize
1. **Analyze Metrics**: Use Grafana to identify bottlenecks.
2. **Optimize Code**: Address performance issues based on analysis.

### Example GitHub Actions Workflow for Load Testing
```yaml:.github/workflows/load_test.yml
name: Load Test

on: [push]

jobs:
  load-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Install JMeter
        run: sudo apt-get install jmeter
      - name: Run JMeter Load Test
        run: jmeter -n -t load_test.jmx -l results.jtl
      - name: Publish Results
        uses: actions/upload-artifact@v2
        with:
          name: jmeter-results
          path: results.jtl
```

By following these steps, you can effectively monitor system performance and resource utilization, identify bottlenecks, and ensure scalability. This approach provides a comprehensive view of system health and performance under different load conditions.