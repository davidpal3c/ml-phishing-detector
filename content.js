chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extractEmail") {
        // ex. get the selected text
        const selectedText = window.getSelection().toString();
        sendResponse({ content: selectedText || "No text selected." });
    }
});