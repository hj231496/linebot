!function(e,t){if("object"==typeof exports&&"object"==typeof module)module.exports=t();else if("function"==typeof define&&define.amd)define([],t);else{var n=t();for(var s in n)("object"==typeof exports?exports:e)[s]=n[s]}}(this,function(){return function(e){var t={};function n(s){if(t[s])return t[s].exports;var r=t[s]={i:s,l:!1,exports:{}};return e[s].call(r.exports,r,r.exports,n),r.l=!0,r.exports}return n.m=e,n.c=t,n.d=function(e,t,s){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:s})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(s,r,function(t){return e[t]}.bind(null,r));return s},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s="81267f17f918cf00a500")}({"172a817d9b61851ddb38":function(e,t,n){"use strict";try{self["workbox:strategies:5.1.3"]&&_()}catch(e){}},"520ae29bd03f91c0cd89":function(e,t,n){"use strict";try{self["workbox:routing:5.1.3"]&&_()}catch(e){}},"7ac768d913c00192a270":function(e,t,n){"use strict";try{self["workbox:core:5.1.3"]&&_()}catch(e){}},"81267f17f918cf00a500":function(e,t,n){"use strict";n.r(t);n("7ac768d913c00192a270");const s=(e,...t)=>{let n=e;return t.length>0&&(n+=` :: ${JSON.stringify(t)}`),n};class r extends Error{constructor(e,t){super(s(e,t)),this.name=e,this.details=t}}const o={googleAnalytics:"googleAnalytics",precache:"precache-v2",prefix:"workbox",runtime:"runtime",suffix:"undefined"!=typeof registration?registration.scope:""},a=e=>[o.prefix,e,o.suffix].filter(e=>e&&e.length>0).join("-"),c={updateDetails:e=>{(e=>{for(const t of Object.keys(o))e(t)})(t=>{"string"==typeof e[t]&&(o[t]=e[t])})},getGoogleAnalyticsName:e=>e||a(o.googleAnalytics),getPrecacheName:e=>e||a(o.precache),getPrefix:()=>o.prefix,getRuntimeName:e=>e||a(o.runtime),getSuffix:()=>o.suffix},i=new Set;const u=e=>{return new URL(String(e),location.href).href.replace(new RegExp(`^${location.origin}`),"")},l=(e,t)=>e.filter(e=>t in e),h=async({request:e,mode:t,plugins:n=[]})=>{const s=l(n,"cacheKeyWillBeUsed");let r=e;for(const e of s)"string"==typeof(r=await e.cacheKeyWillBeUsed.call(e,{mode:t,request:r}))&&(r=new Request(r));return r},f=async({cacheName:e,request:t,event:n,matchOptions:s,plugins:r=[]})=>{const o=await self.caches.open(e),a=await h({plugins:r,request:t,mode:"read"});let c=await o.match(a,s);for(const t of r)if("cachedResponseWillBeUsed"in t){const r=t.cachedResponseWillBeUsed;c=await r.call(t,{cacheName:e,event:n,matchOptions:s,cachedResponse:c,request:a})}return c},d={put:async({cacheName:e,request:t,response:n,event:s,plugins:o=[],matchOptions:a})=>{const c=await h({plugins:o,request:t,mode:"write"});if(!n)throw new r("cache-put-with-no-response",{url:u(c.url)});const d=await(async({request:e,response:t,event:n,plugins:s=[]})=>{let r=t,o=!1;for(const t of s)if("cacheWillUpdate"in t){o=!0;const s=t.cacheWillUpdate;if(!(r=await s.call(t,{request:e,response:r,event:n})))break}return o||(r=r&&200===r.status?r:void 0),r||null})({event:s,plugins:o,response:n,request:c});if(!d)return;const p=await self.caches.open(e),g=l(o,"cacheDidUpdate"),m=g.length>0?await f({cacheName:e,matchOptions:a,request:c}):null;try{await p.put(c,d)}catch(e){throw"QuotaExceededError"===e.name&&await async function(){for(const e of i)await e()}(),e}for(const t of g)await t.cacheDidUpdate.call(t,{cacheName:e,event:s,oldResponse:m,newResponse:d,request:c})},match:f},p={fetch:async({request:e,fetchOptions:t,event:n,plugins:s=[]})=>{if("string"==typeof e&&(e=new Request(e)),n instanceof FetchEvent&&n.preloadResponse){const e=await n.preloadResponse;if(e)return e}const o=l(s,"fetchDidFail"),a=o.length>0?e.clone():null;try{for(const t of s)if("requestWillFetch"in t){const s=t.requestWillFetch,r=e.clone();e=await s.call(t,{request:r,event:n})}}catch(e){throw new r("plugin-error-request-will-fetch",{thrownError:e})}const c=e.clone();try{let r;r="navigate"===e.mode?await fetch(e):await fetch(e,t);for(const e of s)"fetchDidSucceed"in e&&(r=await e.fetchDidSucceed.call(e,{event:n,request:c,response:r}));return r}catch(e){for(const t of o)await t.fetchDidFail.call(t,{error:e,event:n,originalRequest:a.clone(),request:c.clone()});throw e}}};n("172a817d9b61851ddb38");const g={cacheWillUpdate:async({response:e})=>200===e.status||0===e.status?e:null};class m{constructor(e={}){if(this._cacheName=c.getRuntimeName(e.cacheName),this._plugins=e.plugins||[],e.plugins){const t=e.plugins.some(e=>!!e.cacheWillUpdate);this._plugins=t?e.plugins:[g,...e.plugins]}else this._plugins=[g];this._fetchOptions=e.fetchOptions,this._matchOptions=e.matchOptions}async handle({event:e,request:t}){"string"==typeof t&&(t=new Request(t));const n=this._getFromNetwork({request:t,event:e});let s,o=await d.match({cacheName:this._cacheName,request:t,event:e,matchOptions:this._matchOptions,plugins:this._plugins});if(o){if(e)try{e.waitUntil(n)}catch(s){0}}else{0;try{o=await n}catch(e){s=e}}if(!o)throw new r("no-response",{url:t.url,error:s});return o}async _getFromNetwork({request:e,event:t}){const n=await p.fetch({request:e,event:t,fetchOptions:this._fetchOptions,plugins:this._plugins}),s=d.put({cacheName:this._cacheName,request:e,response:n.clone(),event:t,plugins:this._plugins});if(t)try{t.waitUntil(s)}catch(e){0}return n}}var w="location-config",y={ADDRESSES:/^.*customers\/addresses$/,CONFIG:/^.*address-service\/form\/default$/},v=[{capture:y.ADDRESSES,handler:new m({cacheName:"location-addresses"}),method:"GET"},{capture:y.CONFIG,handler:new m({cacheName:w}),method:"GET"}];n("520ae29bd03f91c0cd89");const q="GET",_=e=>e&&"object"==typeof e?e:{handle:e};class R{constructor(e,t,n=q){this.handler=_(t),this.match=e,this.method=n}}class b extends R{constructor(e,t,n){super(({url:t})=>{const n=e.exec(t.href);if(n&&(t.origin===location.origin||0===n.index))return n.slice(1)},t,n)}}class x{constructor(){this._routes=new Map}get routes(){return this._routes}addFetchListener(){self.addEventListener("fetch",e=>{const{request:t}=e,n=this.handleRequest({request:t,event:e});n&&e.respondWith(n)})}addCacheListener(){self.addEventListener("message",e=>{if(e.data&&"CACHE_URLS"===e.data.type){const{payload:t}=e.data;0;const n=Promise.all(t.urlsToCache.map(e=>{"string"==typeof e&&(e=[e]);const t=new Request(...e);return this.handleRequest({request:t})}));e.waitUntil(n),e.ports&&e.ports[0]&&n.then(()=>e.ports[0].postMessage(!0))}})}handleRequest({request:e,event:t}){const n=new URL(e.url,location.href);if(!n.protocol.startsWith("http"))return void 0;const{params:s,route:r}=this.findMatchingRoute({url:n,request:e,event:t});let o=r&&r.handler;if(!o&&this._defaultHandler&&(o=this._defaultHandler),!o)return void 0;let a;try{a=o.handle({url:n,request:e,event:t,params:s})}catch(e){a=Promise.reject(e)}return a instanceof Promise&&this._catchHandler&&(a=a.catch(s=>this._catchHandler.handle({url:n,request:e,event:t}))),a}findMatchingRoute({url:e,request:t,event:n}){const s=this._routes.get(t.method)||[];for(const r of s){let s;const o=r.match({url:e,request:t,event:n});if(o)return s=o,Array.isArray(o)&&0===o.length?s=void 0:o.constructor===Object&&0===Object.keys(o).length?s=void 0:"boolean"==typeof o&&(s=void 0),{route:r,params:s}}return{}}setDefaultHandler(e){this._defaultHandler=_(e)}setCatchHandler(e){this._catchHandler=_(e)}registerRoute(e){this._routes.has(e.method)||this._routes.set(e.method,[]),this._routes.get(e.method).push(e)}unregisterRoute(e){if(!this._routes.has(e.method))throw new r("unregister-route-but-not-found-with-method",{method:e.method});const t=this._routes.get(e.method).indexOf(e);if(!(t>-1))throw new r("unregister-route-route-not-registered");this._routes.get(e.method).splice(t,1)}}let O;const E=()=>(O||((O=new x).addFetchListener(),O.addCacheListener()),O);function N(e){e.forEach(function(e){!function(e,t,n){let s;if("string"==typeof e){const r=new URL(e,location.href);s=new R(({url:e})=>e.href===r.href,t,n)}else if(e instanceof RegExp)s=new b(e,t,n);else if("function"==typeof e)s=new R(e,t,n);else{if(!(e instanceof R))throw new r("unsupported-route-type",{moduleName:"workbox-routing",funcName:"registerRoute",paramName:"capture"});s=e}E().registerRoute(s)}(e.capture,e.handler,e.method)})}var S="SERVICE_WORKER:REMOVE_CACHE";(function(){addEventListener("message",function(e){switch(!0){case e.data.name===S:e.data.data.map(function(e){return caches.delete(e)})}}),N(v),self.addEventListener("activate",function(e){self.skipWaiting(),e.waitUntil(caches.keys().then(function(e){return Promise.all(e.map(function(e){return caches.delete(e)}))}).then(function(){console.log("V2 now ready to handle fetches!")}))})}).apply(void 0)}})});