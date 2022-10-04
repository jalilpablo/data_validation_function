❌GARBAGE IN, GARBAGE OUT❌
Is essential in any ETL process to validate the data, before loading it to the Warehouse.
This simple function checks if, after the extract stage, the Dataframe we are working with, contains data, if the Primary Key has only unique values and if there are any NaN values. Common denominators to any ETL process, to which must be added the specific checks.
This guarantees, after the load stage, that the Analytics and Machine Learning Process are feeded with clean data.

---

❌BASURA ENTRA, BASURA SALE❌
Una parte esencial de cualquier proceso de ETL es la validación de los datos, antes de la carga al Warehouse.
Esta simple función corrobora que, luego de el proceso de extracción, el DataFrame con el que estemos trabajando contenga datos, que no se repita ningún valor en el campo de Clave Primaria y que no contenga valores nulos. Son simples chequeos, genéricos para cualquier proceso de ETL a los que se les deben agregar los específicos de los datos en cuestión.
Esto garantiza, que luego de la etapa de carga, los procesos de Analytics y Machine Learning sean alimentados con datos limpios, sin contaminaciones.
