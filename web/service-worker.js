const cacheName = "renpy-web-game";
const buildUid = "2023-10-16T06:26:13.358Z";
const buildUidCacheKey = "buildUid";
const hostname = self.location.hostname;
const notIncludesHostnameRegex = new RegExp(`^(?!.*${hostname}).*`);
const excludeFromCache = [
    /google-analytics.com/,
    /^(?!http).*/,
    /prelaunch.js/,
    /service-worker.js/,
    /service-worker-pre.js/,
    /api.ascent.lol/,
    notIncludesHostnameRegex,
];

/* Start the service worker and cache all of the app's content or use the existing one */
self.addEventListener("install", async function (e) {
    console.log("Service worker installed.");
    self.skipWaiting();
});

self.addEventListener("activate", async function (e) {
    console.log("Service worker activated.");
    await self.clients.claim();
    await checkCacheStale();
});

async function checkCacheStale() {
    const cache = await caches.open(cacheName);
    const prevBuildUidResponse = await cache.match(buildUidCacheKey);
    const prevBuildUid = !!prevBuildUidResponse ? await prevBuildUidResponse.text() : null;
    console.log("prevBuildUid", prevBuildUid, "buildUid", buildUid);
    const buildUidResponse = new Response(buildUid);

    const isBuildUidStale = !!prevBuildUid && prevBuildUid != buildUid;
    if (isBuildUidStale) {
        console.log("Cache stale, clearing.");
        await caches.delete(cacheName);
        const cache = await caches.open(cacheName);
        await cache.put(buildUidCacheKey, buildUidResponse);
        await messageClients("reload");
    } else {
        console.log("Cache is up to date.");
        await cache.put(buildUidCacheKey, buildUidResponse);
    }
}

async function messageClients(msg) {
    console.log("sending message to clients", msg);
    const clients = await self.clients.matchAll({
        includeUncontrolled: true,
        type: "window",
    });
    for (const client of clients) {
        client.postMessage(msg);
    }
}

async function fetchAndCache(request) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
        // console.log("Served from cache: " + request.url);
        return cachedResponse;
    }

    try {
        const response = await fetch(request);

        if (response.status == 200) {
            // console.log("Served from web: " + request.url, "Adding to cache.");
            await cache.put(request, response.clone());
        }

        return response;
    } catch (e) {
        console.log("Failed to fetch: " + request.url);
        throw e;
    }
}

self.addEventListener("fetch", function (e) {
    if (excludeFromCache.some((re) => re.test(e.request.url))) {
        // console.log("Excluded from cache: " + e.request.url);
        // request will be fetched normally
        return;
    }

    // console.log("Trying to fetch and cache: " + e.request.url);
    e.respondWith(fetchAndCache(e.request));
});

self.addEventListener("message", function (e) {
    // if (e.data[0] == "clearCache") {
    //     caches.delete(cacheName);
    //     console.log("Cache cleared in service worker.");
    //     addToCache = false;
    // } else if (e.data[0] == "loadCache") {
    //     addToCache = true;
    // }
});
