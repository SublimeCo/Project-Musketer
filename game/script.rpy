# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define s = Character("Star")
define m = Character("Matt")
define u = Character("¿¿??")
define r = Character("Rupert")

#All Backgrounds
image cuartoNoche = im.Scale("backgrounds/bg room.jpg", 1280,720)
#All Sprites
image StarHappy = im.Scale("sprites/Star Happy.png",550,750)
image StarBlushed = im.Scale("sprites/Star Blushed.png",550,750)
image StarSerious2 = im.Scale("sprites/Star Serious 2.png",550,750)
image StarSerious = im.Scale("sprites/Star Serious.png",550,750)
image StarSerious3 = im.Scale("sprites/Star Serious 3.png",550,750)
image StarSurprised2 = im.Scale("sprites/Star Surprised 2.png",550,750)
image StarSurprised = im.Scale("sprites/Star Surprised.png",550,750)
image StarWorried2 = im.Scale("sprites/Star Worried 2.png",550,750)
image StarWorried = im.Scale("sprites/Star Worried.png",550,750)
#All OST
define audio.Hanging = "music/OST/Tema 01 - Hanging out (Official).wav"
define audio.Snake = "music/OST/Tema 02 - Snake tongue.wav"
define audio.Memories = "music/OST/Tema 03 - Memories.wav"
# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo:

    scene cuartoNoche

    # Muestra un personaje:

    #show Star1

    # Presenta las líneas del diálogo.

    "Otra noche más... La rutina de siempre presentándose, pero con una pequeña diferencia: la lluvia.\nRecuerdos vagos pasan por mi mente mientras me acomodo en la silla de mi oficina recordándome lo que tristemente hice ayer mientras “disfrutaba” mi día libre. De pronto una molesta sensación se presenta en mi vejiga."
    m "Tengo que ir al baño."
    "Me dirijo hacia la puerta mientras pienso en algunas cosas que han pasado en estos últimos días. La manija de mi vieja puerta está un poco atascada, aunque me las ingenio para no tener que lidiar con ella."
    "Me pregunto si necesito darle un poco de mantenimiento a mi humilde bufete, después de todo también es mi hogar. Podría pintar las paredes con algo de pintura rosa. ¿Pintura rosa? Jajaja, no claro que no, es muy femenino; un negro o café quedaría bien, pero lo dejaré para otra ocasión."
    m "O quizá un color morado."
    show StarHappy
    s "Matt, ¿estás bien?"
    "Demonios, no me fijé en la presencia de Star"
    m "¿Qué? Oh, yo... Sí, estoy bien. Gracias."
    "Bien pensado “genio”. Star me examina con incredulidad."
    s "Bien. Dejaré estos documentos en tu escritorio."
    "Seguramente piensa que estoy loco. Después de todo no tengo nada más que hacer además de revisar el periódico, particularmente la sección policiaca donde la mayoría de veces todo termina en pena de muerte. Star analiza mi condición, su mirada es concentración pura. Para distraerla, y como no estoy muy seguro de si la tensión se debe a su escaneo o a mi vejiga reclamando, hago una mueca y exclamo con gracia:"
    m "Disculpa, ¿planeas tardar mucho? Porque hay un asuntillo por aquí que no da tanta espera..."
    "Star ladea la cabeza en un gesto de confusión. Claro, ella jamas entenderá lo que es una vejiga a punto de estallar. Señalo tras de mí con urgencia."
    m "Ba-ño."
    "Separo las sílabas con claridad y después de procesarlo unos segundos, Star sonríe levemente y señala, como dejándome ir. Me despido de ella rápidamente y me dirijo al baño, voy hacia el retrete y siento una breve satisfacción. Cierro el zipper de mi pantalón y me concentro en escuchar el solitario tic tac del reloj en este cuarto un poco amplio."
    "Ello trae a mi memoria una vez, en la clase de ciencias de la preparatoria, cuando el maestro nos puso a debatir sobre si en el espacio exterior podía haber sonido. Unos decían que no ya que, al no haber aire, el sonido no tendría forma de moverse; otros opinaban que aunque sí sería posible, el sonido sería poco audible. Por mi parte, yo me limité a escucharlos, escribirle una nota a la chica de dos filas más adelante y lanzársela disimuladamente. “Cuando te lleve al espacio, te diré que me gustas. Ya veremos si me oyes o no ;)”. Ella se giró y me sonrió."
    "En fin… Ahora solo soy yo y este viejo reloj, que con su ordinario tic tac y los buenos recuerdos que trae consigo, logra calmar mis sentidos. Termino de lavarme las manos y me enjuago la cara. Me observo fijamente al espejo del baño. Así que este soy yo después de todo."
    m "Ha pasado mucho tiempo, mira cómo he crecido. Ojalá aún estuvieras aquí..."
    "Murmuro tristemente y después regreso a la realidad que me está esperando fuera del baño."
    "Salir a pasear con el sonido de la lluvia alivia mi aburrimiento desde niño. Recuerdo que mi padre me animaba a salir en esas condiciones climatológicas con tal de no dejarme solo en casa. ¿Surgirá efecto si lo intento hoy? Los años han transcurrido, pero supongo que no pierdo nada intentándolo."
    "Mi reloj marca las 11:24 p.m., tal vez sea un poco tarde y peligroso para salir... Por cierto, ¿dónde dejé el paraguas? ¡Bingo!, está junto al perchero ubicado por la puerta principal. Lo tomo al igual que mi abrigo; ahí afuera hay mucho frío y no quisiera amanecer enfermo."
    s "¿Matt?"
    "Probablemente notó que voy a salir. Un paraguas en mano y un abrigo puesto delatan mi plan en marcha."
    m "Disculpa, solo iré a dar una caminata. En una hora estoy de vuelta."
    s "En ese caso… ¿crees que pueda ir contigo?"
    "De hecho tenía planeado hacerlo solo, aunque un poco de compañía no estaría mal. La lluvia no cesa y Star me mira curiosa. Siento que debería llevarla pero... Quería que esta caminata fuera entre la noche y yo. Trato de leer su expresión, pero la intensidad en sus ojos me pone nervioso. Como sea, ¿qué debería hacer?"

    menu:
        "Llevar conmigo a Starfire.":
            jump Llevar_Starfire
        "Irme solo.":
            jump Irme_Solo

    label Llevar_Starfire:

        "Starfire es el prototipo de un proyecto destinado a la interpretación de los sentimientos humanos, tarea que ejecuta a la perfección gracias al trabajo de los mejores ingenieros, quienes la dotaron de esta capacidad que la ha convertido en la musketer más poderosa de entre los siete. Su sistema se centra en una serie de los más finos algoritmos que codifican el comportamiento y las relaciones sinápticas del individuo para arrojar apreciaciones psicológicas con un grado de confiabilidad del 99.9\%, hazaña catalogada como “la base hacia una mejor sociedad”, en la que por fin se pueda comprender objetivamente un aspecto tan subjetivo como la emocionalidad."
        "Debo admitir que esta habilidad siempre me ha despertado una fascinación más allá del profesionalismo. No se reduce a declarar con datos y fundamentos científicos irrefutables, por ejemplo, que el culpable cometió el crimen llevado por la ira, la tristeza, la necesidad, la desesperación o el miedo, y llegar a una condena justa; es esa forma de convertir en números a la humanidad misma y de ensamblar a la perfección dos aspectos que, en teoría, no tendrían por qué ir tan de la mano: razón y sentimientos."
        "Wow, en realidad soy muy afortunado de tener a Star a mi lado... Incluso en momentos incómodos como este en los que me pierdo en mis reflexiones y le doy tiempo de sobra para analizarme y llegar a quién sabe qué clase de juicios, 99.9\% acertados, sobre mis emociones."
        "Sacudo la cabeza cuando caigo en cuenta y le sonrío amigablemente."
        m "Si no te queda nada más por archivar, ¡por supuesto que puedes venir!"
        "Verla un poco tímida se me hace gracioso."
        s "P-pues... Hace dos semanas que no tenemos casos por archivar, entonces..."
        "Me río con ganas."
        m "Claro que no, Star, ese es el punto."
        "Le doy un guiño y estoy seguro de que si tuviera sangre que pudiera subirle a las mejillas, mi querida musketer ya estaría roja como un tomate."
        m "¿Te importaría tomar las llaves de la puerta que están en mi habitación, por favor?"
        "Ella se dirige rápidamente a hacer lo que le pido, por lo que procedemos a salir del bar y bajar por las escaleras, teniendo en cuenta que vivimos en el segundo piso de un edificio, afortunadamente, nuestra molesta recepcionista no está presente debido a la hora."
        s "¿Haces esto cuando llueve?"
        m "Lo hacía de niño junto a mi padre…"
        s "¿Entonces qué te motiva para intentarlo otra vez? "
        m "No lo sé, pero prefiero esto que mi oficina. ¿Tú no harías lo mismo?"
        s "Seguramente…"
        "Se queda callada por unos segundos, para después soltar de golpe, como si se hubiera quedado con una duda atorada."
        s "Pero repetir una determinada acción que se realizaba en ciertas condiciones, las cuales ya no pueden cumplirse, evoca el recuerdo e intensifica el aspecto faltante por encima del acto en sí. El resultado es un sentimiento negativo, de tristeza y añoranza por ese ámbito perdido e irrecuperable."
        "Justo a eso me refiero: racionalización de la emocionalidad. Aun así, su comentario logra sacarme una sonrisa y no puedo evitar que mis siguientes palabras salgan teñidas del cariño y la ternura que me inspira explicarle un sentimiento a la experta en sentimientos."
        m "Se le llama nostalgia, Star. Y no es un sentimiento negativo, si sabes manejarlo adecuadamente. Puedo recordar a mi padre y extrañarlo con todo mi ser, obviamente, pero no tiene que ser con tristeza, sino todo lo contrario, con la alegría de saber que compartí momentos hermosos con él."
        s "Sí, pero ya no podrás hacerlo de nuevo. Perdido e irrecuperable. No puedes experimentar alegría, no tiene ningún sentido."
        m "Quizá no plenamente."
        s "Se experimenta tristeza."
        m "No plenamente."
        s "Pero..."
        m "Ya te lo dije. Se le llama nostalgia y es una mezcla entre ambos. Deberías integrarlo a esa base de datos."
        "Le doy un golpecito juguetón en la cabeza, pero ella no me hace caso."
        s "El término proviene del latín nóstos que quiere decir “regreso”, y álgos, “dolor”. El dolor no puede implicar alegría, Matt."
        "Pongo los ojos en blanco. He aquí el 0.1\% de su margen de error. Sin embargo, decido que es demasiado desgaste seguir discutiendo con ella."
        m "Bien, Dra. Corazón, lo que usted diga."
        "Me parece que está a punto de reclamar, pero al final opta por mantenerse en silencio y yo solo río para mis adentros."
        "Varios metros más adelante, un espectáculo silencioso se revela ante nosotros: la calle desolada, la tenue luz amarilla de las farolas, las gotas de agua cayendo del cielo oscuro, dos niños bajo un tejado bailando con sus luces de bengala al compás de la noche, y un gato negro observándolos de manera minuciosa; esto no es digno de ver por unos simples ojos mortales."
        "La lluvia amansa mis pensamientos, la escena en su conjunto proyecta mi niñez y siembra paz. Starfire analiza el entorno (algo típico en ella); sumado a todo, el color de sus ojos violetas y la mezcla de negros y grisáceos de la sombra me cautivan."
        "Me fijo entonces en que de la tienda de conveniencias “La Duquesa” va saliendo un individuo… Es mi vecino Rupert Stone, quien al parecer compró comida para la cena. Pasamos por su lado limitándonos a un saludo cordial; no es el momento para entablar una charla y, además, parece que Rupert tiene prisa."
        "Una fuerte brisa sopla, haciendo que el frío aumente notablemente. Star se percata de mi sensación, debido a mi movimiento frotando las manos, y se acerca un poco más para compartirme su calor."
        s "¿Te sientes mejor así?"
        "Me mira con un toque de preocupación y yo le doy una sonrisa de agradecimiento."
        m "Sí, creo que así está bien."
        "Continuamos con nuestro recorrido hasta llegar a un puente. Un coche pasa a nuestro lado y su luz me ciega momentáneamente; me detengo a la mitad y, tras recuperarme, me recargo contra el frío barandal y observo el agua correr por debajo de la estructura."
        "Recuerdos y más recuerdos transitan en mi mente. Después de la breve conversación con Star al respecto, quizá puedo profundizar un poco. Empiezo a hablar suavemente, con confianza y tranquilidad."
        m "Cuando tenía siete años, solíamos salir en medio de la lluvia. Mientras mi madre se quedaba en casa descansando luego de haber terminado sus quehaceres, mi padre me enseñaba algunos trucos como hacer barquitos de papel y colocarlos en el agua..."
        "Suspiro y cierro mis ojos, tratando de conseguir una proyección de lo que narro en mi mente. Cuando los vuelvo a abrir, Starfire observa su muñeca y se prepara para hablar."
        s "Las cosas cambian, ¿no es así?"
        "Esta vez no hay referencias técnicas, ni análisis profundo, ni nada por el estilo. Es un comentario tan sencillo y casual que me hace esbozar una leve sonrisa."
        m "Así es."
        "Asiento, meto una mano en el bolsillo al costado de mi pantalón y asevero lo que ya le dije minutos antes."
        m "Me causa nostalgia pensar en mi niñez."
        "Star hace una pequeña mueca, como si no quisiera meterse con esa palabra de nuevo."
        s "Y... Según tú, ¿eso es algo positivo, no?"
        "Sonrío con muchas más ganas por la forma en la que parece dolerle ceder terreno así no esté de acuerdo, solo para dejarme expresar."
        m "Según yo, sí. Pero en realidad también tenías razón hace un instante; todo depende del motivo y de la manera en la que sepas lidiar con ello. Algunas personas lo usan para lastimarse a sí mismas, a tal grado de hundirse en la depresión. Lo he visto en algunos casos."
        "Lo reflexiono durante unos segundos."
        m "Supongo que les gusta el dolor, después de todo; la palabra depresión en su vocabulario está definida de una manera diferente."
        "El humano es un enigma para sí mismo. Este tipo de comportamiento ha sido descrito por psicólogos de mi antigua universidad como un placer, algo bastante bizarro para mi punto de vista..."
        "Star me sorprende al sonreír e imitar mi tono de “ven, te explico”."
        s "Se le llama melancolía, Matt. Los sentimientos humanos pueden llegar a ser un problema si no son controlados. Un episodio anímico de tristeza puede terminar en un estado permanente de sosiego, desinterés y depresión, incluso convertirse en una patología; y ya sabes lo que pasa entonces. El móvil real de cualquier crimen no es la situación que lo provoca, sino una emoción desaforada. Envidia, celos, dolor, furia... Son esos los detonantes de una verdadera catástrofe."
        "No puedo hacer nada más que guardar silencio."
        s "¿Será que nadie los comprende? A veces creo que ustedes mismos se hacen tan insensibles a su propia raza, aun cuando deberían entenderlo mejor que yo... No puedo juzgarlos, no conozco los motivos detrás de sus actos, de sus sentimientos. Aunque cabe la posibilidad de que su capacidad de razonamiento sea inferior a la de un humano promedio y por ello se dejen arrastrar por sus emociones. En todo caso, no depende de ellos, son causas ajenas a su voluntad."
        "Ella me mira buscando aprobación y, puesto que yo estoy demasiado ocupado procesando sus palabras como para dársela, mira hacia el horizonte."
        s "Ustedes los humanos son sorprendentes."
        "Todavía me mantengo un rato callado, antes de decidir que es mejor relajar el ambiente en vez de ponerme a competir con la profundidad de sus consideraciones."
        m "Bueno, algunas veces nos proponemos superar a la ficción."
        "Lo logro. La expresión de Star se suaviza y una sonrisa se apodera de sus labios."
        s "En fin… Solo relajémonos, ¿okay?"
        m "Totalmente de acuerdo contigo."
        "Luego de esa charla, nos quedamos parados disfrutando de la vista aproximadamente unos 30 minutos. Mañana será un nuevo día, así que es hora de irse a casa. La lluvia ha cesado y el cielo se ha ido despejando poco a poco, revelando a una hermosa luna que hoy parece tener dibujado a un conejo apretándose el estómago. Sonrío ante esa imagen y lo desarrollada que tengo mi imaginación; debo ser el único que convierte las manchas de nuestro satélite en un conejo con problemas digestivos."
        m "Vamos Star, creo que ya es hora de regresar."
        "Ella suspira y asiente."
        s "¿Tienes planes para mañana?"
        m "Sí, hay algunos pendientes que no terminé la semana pasada. Por cierto, programa tu despertador a las 8:00 a.m. El tráfico a primeras horas de la mañana es leve."
        s "Vale, me aseguraré de ello."
        m "Perfecto."
        "Observo mi reloj, el cual marca la 1:17 a.m"
        s "¿Vamos?"
        "Cruzamos nuestros brazos y nos dirigimos a casa. Fue buena idea llevar a Starfire, su compañía me ha hecho bien. Si tuviera la oportunidad de darle nombre a este momento, le llamaría “Ideología de una noche perfecta (para Matt)”."


    
    label Irme_Solo:

        "Creo que ahora lo más conveniente es ir sin ella. Estar solo me ayuda a reflexionar mejor y a sumergirme en mis pensamientos sin preocuparme por nada más."
        m "Bueno, en realidad... Si no te molesta, creo que tendrá que ser en otra ocasión. Discúlpame."
        "Star me mira apenada, como si hubiera propuesto algo impensable."
        s "N-no, discúlpame tu a mí, no debí… Lo siento, en serio, y-yo..."
        "Siento una punzada de culpabilidad y me apresuro a explicarle."
        m "No, no, tranquila. No tiene nada malo, no es por... "
        "Suspiro y cierro los ojos un segundo."
        m "Es solo que solía hacer esto con mi padre."
        "Star parece comprender en el acto porque sus ojos adquieren un tinte de tristeza y su tono se hace suave y dulce."
        s "Oh, claro. Descuida. Como sea, ¿estás seguro con la hora programada que me pediste?"
        m "A las 8:00 a.m., ¿cierto?"
        s "Sí."
        m "Está bien, te veré a esa hora entonces. Buenas noches, Star."
        s "Buenas noches, Matt."
        "La observo mientras se retira. Siento pena por negarme, aunque tengo mis razones para no llevarla: este es un momento que tengo que vivir por mi cuenta. Abro la puerta, me encamino a bajas las escaleras de nuestro edificio y me topo con la acera."
        "La fuerte lluvia azota los tejados de aluminio, el viento mece brutalmente las palmeras del vecino vegano y ríos de agua inundan las calles a causa de los árboles que sueltan sus hojas tapando los drenajes. Sigo caminando, esta vez con la mirada hacia abajo; la oscuridad rodea todas las calles. Aullidos de lobos se escuchan sin dejar una pista de su origen mientras que mis pisadas salpican mis zapatos. Empiezo a dudar si fue buena idea hacer esto, pues el ambiente amenaza con transformar mi nostalgia en melancolía y depresión..."
        "La ciudad es distinta por las mañanas, los habitantes abarrotan las calles con sus vehículos y contaminan el aire con smog, el ruido de la vida cotidiana se hace presente en cada esquina y el ritmo acelerado de cada quien en sus asuntos parece no dar tregua. En cambio, por las noches no hay transportes obstruyendo el camino, lo cual ahorra mucho tiempo para desplazarse; lo único que se escucha es el susurro del viento y, hoy, el repiqueteo de las gotas de lluvia; además, a excepción de algunos pensadores nocturnos, como fotógrafos y pintores que se inspiran en la vista para sus obras, no transita ni un alma. Pero hoy solo es un hombre atormentado por sus recuerdos caminando en una ciudad fantasma."
        "El monumento de una tuerca me indica que he llegado al parque."
        m "El único sobreviviente de mis recuerdos."
        "Acaricio la tablilla con una breve inscripción y continúo hasta dar con una farola que me invita a sentarme en el banco junto a sí; coloco el paraguas, seco con mi bufanda el lugar donde me voy a sentar y me acomodo."
        "Este parque ha sido víctima de muchos cambios y remodelaciones. Se supone que enfrente de la farola debería haber un columpio, detrás de mí un sube y baja, y así con tantas otras atracciones que fueron retiradas para dar espacio a las construcciones aledañas."
        "De pronto visualizo el columpio inexistente, yo en él siendo un pequeño y mi padre empujándome con la sonrisa estampada en el rostro. Mi memoria me permite escuchar con claridad nuestras voces alegres, nuestras risotadas cada vez que alcanzo el punto más alto, y el sonido de los niños a nuestro alrededor, practicando algún deporte o jugando en las atracciones. Poco a poco, la escena se desvanece entre la frágil neblina."
        u "Matt."
        "Escucho una voz a mi derecha."
        r "Matt, ¿qué tal?"
        "Me levanto y saludo a mi vecino y amigo Rupert Stone. Corro el paraguas para hacerle un espacio en el banco y seco su lugar mientras él se quita el impermeable que lleva puesto."
        m "Siéntate aquí."
        r "Ah, gracias. Caminar mucho me cansa. ¿Gustas un puro?"
        "Rupert me extiende una cajetilla de puros, pero niego con la cabeza. Él retira uno encogiéndose de hombros, lo prende y empieza a fumar. El olor y el humo se mezclan con las gotas de lluvia, algo que también me hace recordar momentos de mi niñez."
        r "¿Qué haces en el parque a esta hora, Matt?"
        m "*Suspiro* Solo vine a tomar un poco de aire."
        r "Te noto un poco deprimido *sorbe puro*."
        m "Solo le estoy dando vueltas a un asunto insignificante. ¿Y tú qué haces aquí?"
        r "Lo mismo que tú."
        m "¿Lo mismo?, ¿a qué te refieres con eso?"
        r "*Sorbe puro* Pensar en esa maldita guerra."
        "Oh, por supuesto. Tengo que contenerme de poner los ojos en blanco; definitivamente no estoy pensando en la guerra y no tengo razón alguna para hacerlo justo ahora."
        r "Antes podía comprar esos puros de -inserte nombre del país-, ahora solo tengo estos puros de mierda. ¿Todo por qué? Por culpa del gobierno y su asqueroso mineral."
        "Rupert se enoja y arruga en su puño la cajetilla que antes me ofreció."
        m "Cálmate, hombre. Al menos tienes algo que fumar, aprovéchalo."
        "Su enfado disminuye y continúa fabricando humo en silencio durante un rato."
        r "Venías a divertirte aquí cada día con tu padre, ¿te acuerdas?"
        "Ahora sí das en el clavo, mi amigo; bastante lejos de la guerra y tus puros..."
        m "Claro que lo recuerdo, y también cuántas veces desinflaste mi balón."
        "Como dato curioso, jamás pagó por esos balones."
        r "¿Y qué hay de la vez que rompiste mi robot?"
        m "Te lo pagué porque fuiste a quejarte con mi madre. No sabes lo que me hizo por culpa tuya."
        r "Bueno, te mentiría si te digo que no, *jejeje*."
        "Qué hijo de… Ojalá estuviera Starfire para darle lo que se merece, es una pena no haberla traído. Sobre lo que me hizo mi madre, es algo que prefiero mantener en el olvido."
        m "Sigues siendo el mismo, excepto cuando estás con tu esposa; te trae entre sus manos."
        "Me permito reír con ganas. La esposa de Rupert es una persona fina y educada, lo cual es casi todo lo contrario a él. En consecuencia, siempre lo corrige cuando comete una falta, dejándolo en ridículo. Es su media naranja, después de todo."
        r "Cuando estés en mis zapatos lo entenderás, abogadito de quinta."
        m "Lo dudo, tu pie es más grande que el mío."
        "Nuestras carcajadas resuenan en medio de la quietud del parque y entonces me doy cuenta de lo mucho que agradezco que su presencia haya logrado sacarme de mi tristeza. Pasamos la noche hablando de nuestras ocurrencias de niños y jóvenes, siempre en medio de risas y reproches burlescos, hasta que después de una larga y grata charla, Rupert me pregunta la hora."
        m "Wow, ya es la 1:34 a.m."
        "Rupert cambia de expresión radicalmente."
        r "¡Demonios! Charlotte me dejará fuera de casa otra vez."
        m "Pensé que ya te habías acostumbrado a dormir afuera."
        r "¡Calla! Te veré mañana, si es que sobrevivo a la noche."
        "Lo despido con una última risotada. Rupert recoge su impermeable y sale disparado del parque, mientras yo decido que también es hora de volver a casa. Me levanto de mi asiento y emprendo la marcha de regreso. Ha sido una noche agradable a fin de cuentas, aun con la lluvia sin cesar."
        "Una vez dentro de mi casa voy a mi cuarto, me tiro sobre el colchón y me acomodo. Me quedo mirando un rato hacia el techo, pensando, antes de sonreír levemente y decir a nadie en particular."
        m "Buenas noches."
        "Cierro los ojos y busco la forma de conciliar el sueño."
        jump AfterScene

label AfterScene:

    # Finaliza el juego:

    return
