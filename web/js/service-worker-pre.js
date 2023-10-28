(async () => {
    navigator.serviceWorker.addEventListener("message", async (e) => {
        const msg = e.data;
        console.log("message from worker", e.data);
        if (msg === "reload") {
            console.log("Reloading page.");
            window.location.reload();
        }
    });

    navigator.serviceWorker.ready.then((registration) => {
        console.log("Service worker ready, preloading.");
        preloadAssets();
    });

    console.log("Registering service worker.");
    navigator.serviceWorker.register("./service-worker.js", { updateViaCache: "none" });
})();
