const mediaObserver = new MutationObserver((mutations) => {
    mutations.forEach(function (mutation) {
        const nodes = Array.from(mutation.addedNodes);
        nodes.forEach((node) => {
            if (node.tagName === "VIDEO" || node.tagName === "AUDIO") {
                // console.log(node.tagName, node);
                node.setAttribute("muted", "");
                node.muted = true;
                node.onplay = () => {
                    // console.log("started playing", node);
                    setTimeout(() => {
                        node.pause();
                        node.currentTime = 0;
                    }, 100);
                };
            } else if (node.tagName === "DIV") {
                if (node.innerText === "Click to play the video.") {
                    node.remove();
                }
            }
        });
    });
});

mediaObserver.observe(document.body, {
    subtree: true,
    childList: true,
});

async function handlePresplashEnd() {
    await fadeOut("#spinner", 200, true);
    await fadeIn("#presplashButton", 200);
    document.getElementById("presplashButton").addEventListener("click", hidePresplash);
}

function hidePresplash() {
    mediaObserver.disconnect();
    unmutePage();
    fadeOut("#presplashContainer", 200, true);
    const itchDomains = ["itch.io", "hwcdn.net"];
    const isItch = itchDomains.some((domain) => window.location.hostname.includes(domain));
    if (isItch) {
        document.getElementById("statusDiv").classList.add("nodisplay");
    }
}

function mutePage() {
    document.querySelectorAll("video, audio").forEach((elem) => {
        elem.muted = true;
        elem.pause();
    });
}

function unmutePage() {
    document.querySelectorAll("video:not([aliya-preload]), audio").forEach((elem) => {
        elem.removeAttribute("muted");
        elem.muted = false;
        elem.onplay = () => {};
        elem.play();
        console.log("playing", elem);
    });
}

//////////////////

async function fadeIn(selector, duration) {
    const element = document.querySelector(selector);
    element.style.transition = "opacity " + duration + "ms";
    element.style.opacity = 1;

    await wait(duration);
}

async function fadeOut(selector, duration, remove = false) {
    const element = document.querySelector(selector);
    element.style.transition = "opacity " + duration + "ms";
    element.style.opacity = 0;

    if (remove) {
        setTimeout(function () {
            element.parentNode.removeChild(element);
        }, duration);
    }

    await wait(duration);
}

async function wait(duration) {
    return new Promise((resolve) => {
        setTimeout(resolve, duration);
    });
}
