# Quiz 2 - Algoritmos y Programación 2122-3
## PARTE 1 (8pts)
### Selección simple (4pts):
Para cada frase, selecciona la respuesta que consideres correcta a partir de lo observado en el siguiente diagrama de clases:

![image](https://user-images.githubusercontent.com/61355794/174217531-3165f556-5cff-42a0-91aa-e15a828972a2.png)


1. La clase Office tiene ___ clases hijas:  
  a. Una  
  b. Dos  
  c. Tres  
  d. Ninguna  
2. Los atributos de la clase Employee son:  
  a. Públicos  
  b. Protegidos  
  c. Privados  
  d. No tiene atributos  
3. La multiplicidad entre Office y Department es de:  
  a. Uno a uno  
  b. Muchos a muchos  
  c. Uno a muchos  
  d. No tiene  
4. Si la clase Office dejara de existir, las clases que se verían afectadas serían:  
  a. Company  
  b. Company y Department  
  c. Department y Headquarter  
  d. Headquarter  


### Construcción de clases (4pts):
A partir del diagrama de clases dado, modela las clases presentes en él. Recuerda utilizar las convenciones y buenas prácticas dadas en clase.

Para los métodos de las clases:
- Los **getters** (es decir, los que comienzan con “get”) deben retornar el atributo al que hacen referencia. Por ejemplo, “getName” va a tener como retorno al atributo “name”.
- Los **setters** (es decir, los que comienzan con “set”) deben recibir como parámetro al nuevo valor del atributo y modificarlo dentro del método. Por ejemplo, “setName” va a recibir un parámetro, y este parámetro actualizará el valor del atributo “name”.

**NO** debe hacerse ningún menú ni operación de CRUD, solo se pide **modelar las clases**.


## PARTE 2 (12pts + 3pts):
En el presente trimestre se celebrarán las elecciones para escoger a nuestra nueva Federación de Centros de Estudiantes (FCE), por lo que la universidad te ha contratado para que programes el módulo referente a las juntas directivas de un software para automatizar el proceso, que le permita registrar a los candidatos y contabilizar los resultados de la elección.

La siguiente información te dará un poco de contexto para la construcción de tus clases:
- Sobre las Juntas Directivas:
  - La FCE tiene dos tipos de juntas directivas: de escuela y general.
  - Las JDs de escuela tienen un Presidente, un Coordinador General y un Tesorero.
  - La JD general tiene, además de los tres miembros listados anteriormente, un Secretario General y un Secretario de Asuntos Internos.
  - Cada junta directiva, además de sus miembros, está asociada a una plancha.
  - Si la JD es de escuela, debe especificarse a qué escuela pertenece.
- Sobre las Planchas:
  - Tienen nombre y número.

El software deberá contar con las siguientes funcionalidades:
- Registrar planchas.
- Registrar Juntas Directivas.
- Ver la información de las planchas con sus JDs.
- Generar resultados: este proceso funcionará de la siguiente manera. La cantidad de votantes de la elección vendrá dada por los últimos cuatro números del carnet del estudiante (es decir, si mi carnet es 20191111234, la cantidad de votantes que voy a usar es 1234). Se utilizará la librería random para generar un número entre 0 y 100 y será el porcentaje de votos que obtuvo una de las dos planchas (cualquiera, queda a su criterio cómo seleccionar a cuál aplicarle este porcentaje). Una vez se obtengan estos dos números, deberán mostrarse los resultados de la votación indicando cuántos votos obtuvo cada plancha y cuál fue la ganadora.
- Al iniciar el programa, debe realizarse automáticamente el registro de las planchas y JDs.
- Debe existir un menú con las opciones de ver información, generar resultados y salir.

**OJO: el registro de las planchas y JDs NO requiere tomar datos por teclado. Esta información viene almacenada en la estructura de datos dada (y en el archivo TXT). Se espera que se tome dicha información y se almacene como objetos para luego ser utilizados en el programa.**

Como requerimientos opcionales (3pts), se plantea lo siguiente:
- Consumir la información a partir del archivo de texto adjunto en vez de usar la de la estructura de datos dada.
- Al final del día (cuando se vaya a cerrar el programa), guardar el resultado de la elección en un archivo de texto nuevo.
