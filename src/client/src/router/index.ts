import { createRouter, createWebHistory } from "vue-router";

import HomePage from "@/pages/home/HomePage.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "Home",
            component: HomePage,
        },
        {
            path: "/products",
            name: "Products",
            component: () => import("@/pages/products/ProductsPage.vue"),
        },
        {
            path: "/about",
            name: "About",
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import("../pages/AboutPage.vue"),
        },
    ],
    scrollBehavior(to, from, savedPosition) {
        if (to.hash) {
            return {
                el: to.hash,
                behavior: "smooth",
                top: 200,
            };
        }

        // return to top
        return { top: 0, behavior: "smooth" };
    },
});

export default router;
