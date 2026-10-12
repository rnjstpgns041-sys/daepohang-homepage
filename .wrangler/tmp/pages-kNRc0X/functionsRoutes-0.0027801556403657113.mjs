import { onRequestGet as __api_stats_js_onRequestGet } from "/home/user/daepohang-homepage/functions/api/stats.js"
import { onRequestPost as __api_t_js_onRequestPost } from "/home/user/daepohang-homepage/functions/api/t.js"

export const routes = [
    {
      routePath: "/api/stats",
      mountPath: "/api",
      method: "GET",
      middlewares: [],
      modules: [__api_stats_js_onRequestGet],
    },
  {
      routePath: "/api/t",
      mountPath: "/api",
      method: "POST",
      middlewares: [],
      modules: [__api_t_js_onRequestPost],
    },
  ]