#!/bin/bash
# Deploy Script for SU-Vereinswebsite
# This script enforces: commit + push before deploy

set -e  # Exit on error

echo "🚀 Starting deployment process..."

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Must run from project root directory"
    exit 1
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Uncommitted changes detected!"
    echo "Files to commit:"
    git status --short
    
    echo ""
    read -p "Enter commit message: " commit_msg
    
    if [ -z "$commit_msg" ]; then
        echo "❌ Error: Commit message required!"
        exit 1
    fi
    
    git add .
    git commit -m "$commit_msg"
    echo "✅ Changes committed"
else
    echo "✅ No uncommitted changes"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push origin main
echo "✅ Pushed to GitHub"

# Build project
echo "🔨 Building project..."
npm run build
echo "✅ Build successful"

# Deploy to server
echo "📡 Deploying to demo-suwebsite/..."
echo "   ⚠️  Target: /demo-suwebsite/ (NOT root!)"
python3 deploy_correct.py
echo "✅ Deployed successfully to demo-suwebsite/!"

echo ""
echo "🎉 Deployment complete!"
echo "   - Committed changes"
echo "   - Pushed to GitHub"
echo "   - Built project"
echo "   - Deployed to demo-suwebsite/"
