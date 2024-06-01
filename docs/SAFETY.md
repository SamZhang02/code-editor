## Code safety

To ensure environment safety and prevent malicious code, I take two approaches.

### File safety

All user codes and executed in a local read-only Docker container to ensure no
code making changes to the host machine's file system, preventing malicious
actions such as deleting local files, or downloading unwanted binaries.

Additionally, processes are run with a memory and CPU usage cap, alongside a
maximum running time of 10 seconds to prevent infinite resource draining.

### SQL Injection

SQL injection is prevented through avoiding the use of raw SQL queries. SQL
queries are generated using sqlalchemy's query generator.
