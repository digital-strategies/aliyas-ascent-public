(async () => {
    document.body.style.visibility = "visible";

    loadScripts();

    async function loadScripts() {
        const scripts = [
            "js/desktopCheck.js",
            "js/preload.js",
            "js/service-worker-pre.js",
            "js/presplash.js",
            "renpy-pre.js",
            "renpy.js",
        ];
        for (const src of scripts) {
            await new Promise((resolve, reject) => {
                const script = document.createElement("script");
                script.src = src;
                script.onload = resolve;
                script.onerror = reject;
                document.body.appendChild(script);
            });
        }
    }
})();
