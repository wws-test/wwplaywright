import sqlglot
print(sqlglot.transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0])