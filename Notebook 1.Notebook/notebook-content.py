# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7ae2b96b-e08a-4906-a61c-aea93553c073",
# META       "default_lakehouse_name": "Contoso",
# META       "default_lakehouse_workspace_id": "897aef99-5f20-4e16-8808-02a38a082d62",
# META       "known_lakehouses": [
# META         {
# META           "id": "7ae2b96b-e08a-4906-a61c-aea93553c073"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import subprocess
subprocess.run(["pip", "install", "py7zr", "-q"], check=True)
print("py7zr installed")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
