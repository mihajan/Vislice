%import model
%rebase('base.tpl', title='Vislice')



  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
  </blockquote>

  <h2> {{ igra.pravilni_del_gesla() }} </h2>

  <h2> Napačnih ugibov: {{igra.nepravilni_ugibi()}} </h2>

   % if poskus == 'w':
     <h1> ZMAGAL SI </h1> 
   % elif poskus == 'x':
     <h1> IZGUBIL SI </h1>
   % else: 

  <img src="img/10.jpg" alt="obesanje">
  
 <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>



  <form action="/igra/" method="post">
   Črka: <input type="text" name="crka" maxlength="1">
   <button type="submit">Ugibaj novo črko</button>
  </form>




 
  </form>
