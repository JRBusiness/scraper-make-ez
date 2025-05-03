Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]});

HTMLCanvasElement.prototype.toDataURL = function() {
    return "data:image/png;base64,spoofed_canvas";
};

const getParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
    if (parameter === 37445) return "Intel Inc.";
    if (parameter === 37446) return "Intel(R) HD Graphics";
    return getParameter(parameter);
};
