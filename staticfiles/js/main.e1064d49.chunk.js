(window.webpackJsonpfront=window.webpackJsonpfront||[]).push([[0],{43:function(e,t,a){e.exports=a(74)},48:function(e,t,a){},71:function(e,t,a){},74:function(e,t,a){"use strict";a.r(t);var n={};a.r(n),a.d(n,"traer_uno",function(){return _}),a.d(n,"agregar_respuesta",function(){return w}),a.d(n,"agregar_respuesta_uno",function(){return k}),a.d(n,"quitar_respuesta",function(){return x}),a.d(n,"agregar_respuesta_texto",function(){return C}),a.d(n,"guardar_datos",function(){return S});var r=a(0),s=a.n(r),c=a(22),o=a.n(c),u=(a(48),a(8)),p=a.n(u),i=a(18),l=a(16),m=a(9),d=a(10),h=a(14),g=a(11),f=a(13),v=a(12),b=a(21),E=a.n(b),y="TRAER_UNO_ENCUESTA",O="GUARDADO_ENCUESTA";function j(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),a.push.apply(a,n)}return a}function N(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?j(a,!0).forEach(function(t){Object(l.a)(e,t,a[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):j(a).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))})}return e}var _=function(e){return function(){var t=Object(i.a)(p.a.mark(function t(a){var n,r,s,c;return p.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,E.a.get("https://www.mktestudios.com/api/v1/encuestas/".concat(e,"/"));case 3:n=t.sent,r=n.data,s=r.preguntas.map(function(e){return N({},e,{respuestas:[],respuesta_texto:""})}),c=N({},r,{preguntas:s}),a({type:y,payload:c}),t.next=13;break;case 10:t.prev=10,t.t0=t.catch(0),console.log(t.t0);case 13:case"end":return t.stop()}},t,null,[[0,10]])}));return function(e){return t.apply(this,arguments)}}()},w=function(e,t){return function(a,n){var r=n().encuestaReducers.encuesta,s=r.preguntas;s[e]=N({},s[e],{respuestas:s[e].respuestas.concat(t)});var c=N({},r,{preguntas:s});a({type:y,payload:c})}},k=function(e,t){return function(a,n){var r=n().encuestaReducers.encuesta,s=r.preguntas;s[e]=N({},s[e],{respuestas:[t]});var c=N({},r,{preguntas:s});a({type:y,payload:c})}},x=function(e,t){return function(a,n){var r=n().encuestaReducers.encuesta,s=r.preguntas,c=s[e].respuestas,o=c.findIndex(function(e){return e.id===t.id});c.splice(o,1),s[e]=N({},s[e],{respuestas:c});var u=N({},r,{preguntas:s});a({type:y,payload:u})}},C=function(e,t){return function(a,n){var r=n().encuestaReducers.encuesta,s=r.preguntas;s[e]=N({},s[e],{respuesta_texto:t});var c=N({},r,{preguntas:s});a({type:y,payload:c})}},S=function(e){return function(){var t=Object(i.a)(p.a.mark(function t(a,n){var r,s,c;return p.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return r=n().encuestaReducers.encuesta,s=[],r.preguntas.forEach(function(e){e.respuestas.length>0?e.respuestas.forEach(function(t){s.push({id_pregunta:e.id,id_opcion:t.id,texto_respuesta:e.respuesta_texto,relacion_pregunta:e.dependencia||0})}):s.push({id_pregunta:e.id,id_opcion:0,texto_respuesta:e.respuesta_texto,relacion_pregunta:e.dependencia||0})}),c={id_encuesta:r.slug,respuestas:s,datos_encuestado:e},t.prev=4,t.next=7,E.a.post("https://www.mktestudios.com/api/v1/respuestas/",c);case 7:a({type:O,payload:"El formulario ha sido guardado correctamente muchas gracias."}),t.next=13;break;case 10:t.prev=10,t.t0=t.catch(4),console.log(t.t0);case 13:case"end":return t.stop()}},t,null,[[4,10]])}));return function(e,a){return t.apply(this,arguments)}}()},D=(a(71),function(){return s.a.createElement("div",{className:"loader"},s.a.createElement("div",{className:"lds-ellipsis"},s.a.createElement("div",null),s.a.createElement("div",null),s.a.createElement("div",null),s.a.createElement("div",null)))}),A=function(e){function t(){var e,a;Object(m.a)(this,t);for(var n=arguments.length,r=new Array(n),s=0;s<n;s++)r[s]=arguments[s];return(a=Object(h.a)(this,(e=Object(g.a)(t)).call.apply(e,[this].concat(r)))).state={ciudades:[]},a.handleChange=function(e){var t=e.target.id,n=e.target.value;a.setState(Object(l.a)({},t,n))},a}return Object(f.a)(t,e),Object(d.a)(t,[{key:"componentDidMount",value:function(){var e=Object(i.a)(p.a.mark(function e(){var t;return p.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,E.a.get("https://www.mktestudios.com/api/v1/ciudades/");case 2:t=e.sent,this.setState({ciudades:t.data.results});case 4:case"end":return e.stop()}},e,this)}));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return s.a.createElement("div",null,s.a.createElement("div",{className:"row"},s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"nombres"},"Nombres"),s.a.createElement("input",{className:"form-control",type:"text",id:"nombres",value:this.props.nombres,onChange:this.props.onChange})),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"apellidos"},"Apellidos"),s.a.createElement("input",{className:"form-control",type:"text",id:"apellidos",value:this.props.apellidos,onChange:this.props.onChange})),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"edad"},"Edad"),s.a.createElement("input",{className:"form-control",type:"number",id:"edad",value:this.props.edad,onChange:this.props.onChange})),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"genero"},"Genero"),s.a.createElement("select",{className:"form-control",type:"text",id:"genero",value:this.props.genero,onChange:this.props.onChange},s.a.createElement("option",{value:"M"},"Maculino"),s.a.createElement("option",{value:"F"},"Femenino"))),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"ciudad"},"Ciudad"),s.a.createElement("select",{className:"form-control",type:"text",id:"ciudad",value:this.props.ciudad,onChange:this.props.onChange},s.a.createElement("option",null,"Seleccione uno"),this.state.ciudades.map(function(e){return s.a.createElement("option",{key:e.id,value:e.id},e.nombre)}))),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"email"},"Correo"),s.a.createElement("input",{className:"form-control",type:"email",id:"email",value:this.props.email,onChange:this.props.onChange})),s.a.createElement("div",{className:"col-md-6 form-check"},s.a.createElement("label",{htmlFor:"tiene_hijos"},"Tiene hijos"),s.a.createElement("select",{className:"form-control",id:"tiene_hijos",value:this.props.tiene_hijos,onChange:this.props.onChange},s.a.createElement("option",{value:""},"Seleccione uno"),s.a.createElement("option",{value:"true"},"SI"),s.a.createElement("option",{value:"false"},"NO"))),s.a.createElement("div",{className:"col-md-6 form-group"},s.a.createElement("label",{htmlFor:"edad"},"Edad hijos"),s.a.createElement("input",{className:"form-control",type:"text",id:"edad_hijos",placeholder:"Ejemplo: 12, 2, 3",value:this.props.edad_hijos,onChange:this.props.onChange}))))}}]),t}(s.a.Component),P=function(e){return s.a.createElement("div",{className:"mensaje"},s.a.createElement("div",{className:"card"},s.a.createElement("div",{className:"card-body"},s.a.createElement("h4",{className:"card-title"},"Muchas Gracias"),s.a.createElement("p",{className:"card-text"},e.mensaje))))},R=function(e){function t(){var e,a;Object(m.a)(this,t);for(var n=arguments.length,r=new Array(n),s=0;s<n;s++)r[s]=arguments[s];return(a=Object(h.a)(this,(e=Object(g.a)(t)).call.apply(e,[this].concat(r)))).state={checked:!1},a.handleClick=function(){a.state.checked?a.props.quitar_respuesta(a.props.pregunta,a.props.opcion):a.props.agregar_respuesta(a.props.pregunta,a.props.opcion),a.setState({checked:!a.state.checked})},a}return Object(f.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){var e=this.props.opcion,t="fa fa-check hidden";return this.state.checked&&(t+="fa fa-check checked-image"),s.a.createElement("div",{className:"col-xs-4 col-sm-3 col-md-3 text-center"},s.a.createElement("button",{type:"button",onClick:this.handleClick,className:"image-check"},s.a.createElement("img",{className:"img-responsive img-op",src:e.imagen,alt:e.imagen}),s.a.createElement("i",{className:t})))}}]),t}(s.a.Component),F=Object(v.b)(null,n)(R),M=function(e){function t(){var e,a;Object(m.a)(this,t);for(var n=arguments.length,r=new Array(n),s=0;s<n;s++)r[s]=arguments[s];return(a=Object(h.a)(this,(e=Object(g.a)(t)).call.apply(e,[this].concat(r)))).handleChange=function(e){var t=e.target.checked;1!==a.props.multiple?t?a.props.agregar_respuesta(a.props.pregunta,a.props.opcion):a.props.quitar_respuesta(a.props.pregunta,a.props.opcion):a.props.agregar_respuesta_uno(a.props.pregunta,a.props.opcion)},a}return Object(f.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){var e=this.props.opcion,t="checkbox";return 1===this.props.multiple&&(t="radio"),s.a.createElement("div",{className:"form-check"},s.a.createElement("input",{className:"form-check-input",type:t,name:this.props.pregunta,id:e.id,value:e.id,onChange:this.handleChange}),s.a.createElement("label",{className:"form-check-label",htmlFor:e.id},e.titulo))}}]),t}(s.a.Component),T=Object(v.b)(null,n)(M),U=function(e){function t(){var e,a;Object(m.a)(this,t);for(var n=arguments.length,c=new Array(n),o=0;o<n;o++)c[o]=arguments[o];return(a=Object(h.a)(this,(e=Object(g.a)(t)).call.apply(e,[this].concat(c)))).handleMultiples=function(e){if(e.filter(function(e){return null!==e.imagen}).length)return s.a.createElement("div",{className:"row"},e.map(function(e,t){return s.a.createElement(F,{key:e.id,opcion:e,pregunta:a.props.pregunta,index:t})}));var t=a.props.encuesta.preguntas[a.props.pregunta].especifica,n=a.props.encuesta.preguntas[a.props.pregunta].respuestas[0],c=!1;return n&&(c=n.especifica),s.a.createElement(r.Fragment,null,a.props.encuesta.preguntas[a.props.pregunta].expecifica,e.map(function(e){return s.a.createElement(T,{key:e.id,opcion:e,pregunta:a.props.pregunta,multiple:a.props.encuesta.preguntas[a.props.pregunta].max_respuestas})}),t&&c?s.a.createElement("div",{className:"form-group"},s.a.createElement("textarea",{className:"form-control",name:"abierto[]",onChange:function(e){return a.props.agregar_respuesta_texto(a.props.pregunta,e.target.value)}})):"")},a.handleMultiplesDependencia=function(){var e=a.props.encuesta.preguntas[a.props.pregunta].dependencia,t=a.props.encuesta.preguntas.findIndex(function(t){return t.id===e}),n=a.props.encuesta.preguntas[t].respuestas;return console.log(n),s.a.createElement("div",{className:"row"},n.map(function(e,t){return s.a.createElement(F,{key:e.id,opcion:e,pregunta:a.props.pregunta,index:t})}))},a}return Object(f.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){var e=this,t=this.props.pregunta;return this.props.encuesta.preguntas[t].respuestas_multiples?this.handleMultiples(this.props.encuesta.preguntas[t].opciones):this.props.encuesta.preguntas[t].dependencia?this.handleMultiplesDependencia():s.a.createElement("div",{className:"form-group"},s.a.createElement("textarea",{className:"form-control",name:"abierto[]",onChange:function(a){return e.props.agregar_respuesta_texto(t,a.target.value)}}))}}]),t}(s.a.Component),I=Object(v.b)(function(e){return e.encuestaReducers},n)(U),G=function(e){function t(){var e,a;Object(m.a)(this,t);for(var n=arguments.length,r=new Array(n),s=0;s<n;s++)r[s]=arguments[s];return(a=Object(h.a)(this,(e=Object(g.a)(t)).call.apply(e,[this].concat(r)))).state={nombres:"",apellidos:"",edad:0,genero:"M",ciudad:"",email:"",tiene_hijos:!1,edad_hijos:""},a.handleSumit=function(e){e.preventDefault(),a.props.guardar_datos(a.state)},a.handleChangeInput=function(e){var t=e.target.id,n=e.target.value;a.setState(Object(l.a)({},t,n))},a}return Object(f.a)(t,e),Object(d.a)(t,[{key:"componentDidMount",value:function(){var e=Object(i.a)(p.a.mark(function e(){return p.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.props.traer_uno(this.props.match.params.slug);case 2:case"end":return e.stop()}},e,this)}));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return console.log(this.props),this.props.cargando?s.a.createElement(D,null):this.props.mensaje?s.a.createElement(P,{mensaje:this.props.mensaje}):s.a.createElement("form",{className:"form-encuesta",onSubmit:this.handleSumit},s.a.createElement("h4",{className:"text-center"},this.props.encuesta.nombre),s.a.createElement("br",null),s.a.createElement(A,Object.assign({onChange:this.handleChangeInput},this.state)),s.a.createElement("br",null),this.props.encuesta.preguntas.map(function(e,t){return s.a.createElement("div",{key:e.id,className:"content-preguntas"},s.a.createElement("h5",null,e.nombre),s.a.createElement("p",{className:"text-muted"},e.descripcion),s.a.createElement(I,{pregunta:t}))}),s.a.createElement("div",{className:"text-center"},s.a.createElement("button",{type:"submit",className:"btn btn-primary"},"Enviar informaci\xf3n")))}}]),t}(s.a.Component),q=Object(v.b)(function(e){return e.encuestaReducers},n)(G),J=a(17),B=function(){return s.a.createElement("div",{className:"container"},s.a.createElement(J.a,{exact:!0,path:"/:slug",component:q}))},z=a(19),H=a(42),K=a(26);a(73);function L(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),a.push.apply(a,n)}return a}function Q(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?L(a,!0).forEach(function(t){Object(l.a)(e,t,a[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):L(a).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))})}return e}var V={encuesta:{},datos_encuestado:{},cargando:!0,mensaje:"",error:""},W=Object(z.c)({encuestaReducers:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:V,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case y:return Q({},e,{encuesta:t.payload,cargando:!1,error:""});case"CARGANDO_ENCUESTA":return Q({},e,{cargando:!0});case"ERROR_ENCUESTA":return Q({},e,{cargando:!1,error:t.payload});case"DATOS_ENCUESTADO":return Q({},e,{datos_encuestado:t.payload});case O:return Q({},e,{encuesta:{},cargando:!1,mensaje:t.payload});default:return e}}}),X=Object(z.d)(W,{},Object(z.a)(H.a));o.a.render(s.a.createElement(v.a,{store:X},s.a.createElement(K.a,null,s.a.createElement(B,null))),document.getElementById("root"))}},[[43,1,2]]]);
//# sourceMappingURL=main.e1064d49.chunk.js.map