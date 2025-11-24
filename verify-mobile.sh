#!/bin/bash

echo "=========================================="
echo "MOBILE RESPONSIVENESS VERIFICATION"
echo "=========================================="
echo ""

echo "1. Checking mobile.css file..."
if [ -f "mobile.css" ]; then
    echo "   ✓ mobile.css exists"
    echo "   - Size: $(wc -c < mobile.css) bytes"
    echo "   - Lines: $(wc -l < mobile.css)"
else
    echo "   ✗ mobile.css NOT FOUND"
fi
echo ""

echo "2. Checking HTML files with mobile.css linked..."
html_count=$(ls -1 *.html 2>/dev/null | wc -l)
mobile_count=$(grep -l "mobile.css" *.html 2>/dev/null | wc -l)
echo "   - Total HTML files: $html_count"
echo "   - Files with mobile.css: $mobile_count"
if [ "$html_count" -eq "$mobile_count" ]; then
    echo "   ✓ All HTML files have mobile.css"
else
    echo "   ⚠ Some files missing mobile.css"
    echo "   Missing files:"
    for file in *.html; do
        if ! grep -q "mobile.css" "$file"; then
            echo "     - $file"
        fi
    done
fi
echo ""

echo "3. Checking mobile menu toggle implementation..."
toggle_count=$(grep -l "mobileMenuToggle" *.html 2>/dev/null | wc -l)
echo "   - Files with mobile menu toggle: $toggle_count"
if [ "$toggle_count" -ge 10 ]; then
    echo "   ✓ Mobile menu widely implemented"
else
    echo "   ⚠ Mobile menu may need more coverage"
fi
echo ""

echo "4. Checking responsive breakpoints in mobile.css..."
breakpoint_768=$(grep -c "@media.*768px" mobile.css 2>/dev/null)
breakpoint_480=$(grep -c "@media.*480px" mobile.css 2>/dev/null)
breakpoint_360=$(grep -c "@media.*360px" mobile.css 2>/dev/null)
echo "   - @media 768px breakpoints: $breakpoint_768"
echo "   - @media 480px breakpoints: $breakpoint_480"
echo "   - @media 360px breakpoints: $breakpoint_360"
if [ "$breakpoint_768" -gt 0 ]; then
    echo "   ✓ Responsive breakpoints configured"
fi
echo ""

echo "5. Key pages verification..."
key_pages=("index.html" "cart.html" "checkout.html" "orders.html" "wishlist.html")
for page in "${key_pages[@]}"; do
    if [ -f "$page" ] && grep -q "mobile.css" "$page"; then
        echo "   ✓ $page is mobile-ready"
    else
        echo "   ✗ $page needs attention"
    fi
done
echo ""

echo "=========================================="
echo "VERIFICATION COMPLETE"
echo "=========================================="
echo ""
echo "To test mobile features:"
echo "1. Open any page in a browser"
echo "2. Press F12 for Developer Tools"
echo "3. Click device toolbar (Ctrl+Shift+M)"
echo "4. Select a mobile device preset"
echo "5. Test the hamburger menu (☰)"
echo ""
echo "Or visit: mobile-test.html for live testing"
