# Git Workflow and Contribution Guidelines

Complete Git workflow documentation for the Government Hostel Management System project.

---

## Table of Contents

1. [Branch Strategy](#branch-strategy)
2. [Branch Naming Convention](#branch-naming-convention)
3. [Commit Message Convention](#commit-message-convention)
4. [Development Workflow](#development-workflow)
5. [Pull Request Process](#pull-request-process)
6. [Merge Policy](#merge-policy)
7. [Branch Cleanup](#branch-cleanup)
8. [Quick Reference](#quick-reference)
9. [Common Scenarios](#common-scenarios)

---

## Branch Strategy

Our project uses a **three-tier branching strategy** to maintain code quality and stability:

### 1. `main` Branch
- **Purpose:** Production-ready, stable code
- **Status:** Always demo-ready
- **Protection:** ❌ No direct commits allowed
- **Updates:** Only merged from `develop` by team lead
- **Use Case:** Deployments, releases, demos

### 2. `develop` Branch
- **Purpose:** Integration branch for ongoing development
- **Status:** Active development, tested features
- **Protection:** ❌ No direct commits allowed
- **Updates:** Merged from `feature/*` branches via Pull Requests
- **Use Case:** Combining completed features before production

### 3. `feature/*` Branches
- **Purpose:** Individual feature development
- **Status:** Work in progress
- **Protection:** ✅ Direct commits allowed
- **Updates:** Created from `develop`, merged back to `develop`
- **Use Case:** All new features, bug fixes, improvements

---

## Branch Naming Convention

All feature branches **must** follow this naming pattern:

```
feature/<short-descriptive-name>
```

### Naming Rules

✅ **Good Examples:**
```bash
feature/ui-auth-setup
feature/ui-student-registration
feature/room-allocation
feature/payment-integration
feature/dashboard-ui
feature/api-endpoints
feature/database-schema
```

❌ **Bad Examples:**
```bash
feature/fix              # Too vague
feature/new_feature      # Not descriptive
myfeature               # Missing 'feature/' prefix
feature/Fix-Bug         # Use lowercase with hyphens
feature/add_students    # Use hyphens, not underscores
```

### Naming Guidelines

- Use **lowercase** letters only
- Separate words with **hyphens** (`-`)
- Keep names **short** but **descriptive**
- Use **2-4 words** maximum
- Describe **what** the feature does, not **how**

---

## Commit Message Convention

Write clear, consistent commit messages using these prefixes:

### Commit Prefixes

| Prefix | Use Case | Example |
|--------|----------|---------|
| `Add:` | New feature or file | `Add: student registration form` |
| `Fix:` | Bug fix | `Fix: login authentication error` |
| `Update:` | Modify existing feature | `Update: dashboard layout design` |
| `Refactor:` | Code restructuring | `Refactor: API service structure` |
| `Docs:` | Documentation changes | `Docs: update setup guide` |
| `Style:` | Code formatting | `Style: format Python files` |
| `Remove:` | Delete code/files | `Remove: unused components` |
| `Test:` | Add or update tests | `Test: add auth service tests` |

### Commit Message Format

```bash
<Prefix>: <brief description in lowercase>

# Optional: Detailed explanation
# - What changed
# - Why it changed
# - Any breaking changes
```

### Examples

✅ **Good Commit Messages:**
```bash
git commit -m "Add: student registration API endpoint"
git commit -m "Fix: resolve CORS error in frontend"
git commit -m "Update: improve dashboard performance"
git commit -m "Docs: add Git workflow documentation"
```

❌ **Bad Commit Messages:**
```bash
git commit -m "fixed stuff"           # Too vague
git commit -m "Added new feature"     # Not descriptive
git commit -m "update"                # Missing prefix
git commit -m "FIX: Login Bug"        # Use lowercase
```

---

## Development Workflow

Follow these steps for all development work:

### Step 1: Start from `develop`

```bash
# Make sure you're on develop branch
git checkout develop

# Get latest changes
git pull origin develop
```

### Step 2: Create Feature Branch

```bash
# Create and switch to new feature branch
git checkout -b feature/your-feature-name

# Example:
git checkout -b feature/student-dashboard
```

### Step 3: Make Changes

```bash
# Work on your feature
# Edit files, write code, test locally

# Check what files changed
git status

# Review your changes
git diff
```

### Step 4: Commit Changes

```bash
# Stage specific files
git add filename1 filename2

# Or stage all changes
git add .

# Commit with clear message
git commit -m "Add: student dashboard component"
```

### Step 5: Push to Remote

```bash
# Push your feature branch to remote repository
git push origin feature/your-feature-name

# Example:
git push origin feature/student-dashboard
```

### Step 6: Create Pull Request

1. Go to GitHub/GitLab repository
2. Click "New Pull Request"
3. Select:
   - **Base:** `develop`
   - **Compare:** `feature/your-feature-name`
4. Fill in PR details:
   - **Title:** Clear, descriptive title
   - **Description:** What changed and why
   - **Screenshots:** If UI changes
5. Submit Pull Request
6. Wait for review

### Step 7: Address Review Feedback

```bash
# Make requested changes
# Edit files based on feedback

# Commit changes
git add .
git commit -m "Update: address PR review comments"

# Push updates
git push origin feature/your-feature-name
```

### Step 8: After Merge

```bash
# Switch back to develop
git checkout develop

# Pull latest changes (includes your merged feature)
git pull origin develop

# Delete local feature branch
git branch -d feature/your-feature-name
```

---

## Pull Request Process

### Creating a Pull Request

**Requirements:**
- ✅ All changes committed
- ✅ Feature branch pushed to remote
- ✅ Code tested locally
- ✅ No merge conflicts with `develop`

**PR Template:**

```markdown
## Description
Brief description of what this PR does

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Done
- [ ] Tested locally
- [ ] No errors in console
- [ ] Feature works as expected

## Screenshots (if applicable)
[Add screenshots here]

## Related Issues
Fixes #issue_number (if applicable)
```

### Review Process

1. **Developer** creates Pull Request
2. **Team Lead** reviews the code
3. **Team Lead** may request changes
4. **Developer** addresses feedback
5. **Team Lead** approves and merges
6. **Feature branch** is deleted

### Review Checklist

Reviewers will check:
- ✅ Code follows project structure
- ✅ No syntax errors
- ✅ Commit messages are clear
- ✅ No unnecessary files committed
- ✅ Feature works as described
- ✅ No conflicts with existing code

---

## Merge Policy

### Rules

1. **Only Team Lead** merges Pull Requests
2. **All merges** go through Pull Request review
3. **No direct commits** to `main` or `develop`
4. **Feature branches** merge into `develop` only
5. **Develop** merges into `main` only at milestones

### Merge Flow

```
feature/auth-setup  ──PR──>  develop  ──Team Lead──>  main
feature/dashboard   ──PR──>  develop  ──Team Lead──>  main
feature/api-setup   ──PR──>  develop  ──Team Lead──>  main
```

### When `develop` Merges to `main`

The team lead merges `develop` into `main` when:
- ✅ A milestone is complete
- ✅ All features are tested
- ✅ Ready for demo/deployment
- ✅ No known critical bugs

---

## Branch Cleanup

### After Successful Merge

**Remote Branch Deletion:**
- Done automatically by GitHub/GitLab after PR merge
- Or manually: `git push origin --delete feature/branch-name`

**Local Branch Deletion:**
```bash
# Switch to develop first
git checkout develop

# Delete local feature branch
git branch -d feature/branch-name

# Force delete if needed
git branch -D feature/branch-name
```

### Recovering Deleted Branches

If you need to recreate a deleted branch:

```bash
# Find the commit hash from history
git log --all --oneline | grep "your feature"

# Create new branch from that commit
git checkout -b feature/branch-name <commit-hash>
```

### Keeping Your Local Repository Clean

```bash
# List all local branches
git branch

# List remote branches
git branch -r

# Remove local branches that are deleted remotely
git fetch --prune

# Delete multiple local branches
git branch | grep "feature/" | xargs git branch -D
```

---

## Quick Reference

### Common Commands

```bash
# Check current branch
git branch

# Switch branch
git checkout branch-name

# Create and switch to new branch
git checkout -b feature/new-feature

# Get latest changes
git pull origin develop

# Stage changes
git add .

# Commit changes
git commit -m "Add: feature description"

# Push changes
git push origin feature/branch-name

# View commit history
git log --oneline

# View changes
git diff

# Discard local changes
git checkout -- filename

# Update from develop while on feature branch
git checkout feature/your-branch
git merge develop
```

### Workflow Cheat Sheet

```bash
# 1. Start new feature
git checkout develop
git pull origin develop
git checkout -b feature/my-feature

# 2. Work and commit
git add .
git commit -m "Add: my feature"

# 3. Push and create PR
git push origin feature/my-feature
# Then create PR on GitHub/GitLab

# 4. After merge, cleanup
git checkout develop
git pull origin develop
git branch -d feature/my-feature
```

---

## Common Scenarios

### Scenario 1: Starting a New Feature

```bash
# Ensure you're on develop
git checkout develop

# Get latest code
git pull origin develop

# Create feature branch
git checkout -b feature/user-profile

# Start coding...
```

### Scenario 2: Saving Work in Progress

```bash
# Stage all changes
git add .

# Commit with WIP message
git commit -m "WIP: user profile component"

# Push to remote (backup)
git push origin feature/user-profile
```

### Scenario 3: Updating Feature Branch with Latest `develop`

```bash
# On your feature branch
git checkout feature/your-feature

# Get latest develop changes
git fetch origin develop

# Merge develop into your feature
git merge origin/develop

# Resolve any conflicts if they occur
# Then commit the merge
git commit -m "Merge: update from develop"

# Push updated branch
git push origin feature/your-feature
```

### Scenario 4: Fixing Merge Conflicts

```bash
# When merge conflict occurs
git status  # See conflicted files

# Open conflicted files and look for:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> develop

# Edit files to resolve conflicts
# Remove conflict markers
# Keep the correct code

# Stage resolved files
git add resolved-file.js

# Complete the merge
git commit -m "Fix: resolve merge conflicts"

# Push changes
git push origin feature/your-branch
```

### Scenario 5: Accidentally Committed to Wrong Branch

```bash
# If you committed to develop instead of feature branch
git checkout develop

# Undo the last commit (keep changes)
git reset --soft HEAD~1

# Create correct feature branch
git checkout -b feature/correct-branch

# Commit again
git add .
git commit -m "Add: feature description"

# Push to correct branch
git push origin feature/correct-branch
```

### Scenario 6: Need to Switch Branches with Uncommitted Changes

```bash
# Option 1: Stash changes
git stash
git checkout other-branch
# Later, return and restore:
git checkout original-branch
git stash pop

# Option 2: Commit as WIP
git add .
git commit -m "WIP: temporary commit"
git checkout other-branch
# Later, return and continue:
git checkout original-branch
```

---

## Best Practices

### Do's ✅

- ✅ Always create feature branches from `develop`
- ✅ Pull latest `develop` before creating new branch
- ✅ Commit frequently with clear messages
- ✅ Push your branch regularly (backup)
- ✅ Test your code before creating PR
- ✅ Keep feature branches focused and small
- ✅ Delete branches after successful merge
- ✅ Ask for help if stuck

### Don'ts ❌

- ❌ Never commit directly to `main` or `develop`
- ❌ Don't create branches from other feature branches
- ❌ Don't commit sensitive data (passwords, keys)
- ❌ Don't commit large binary files
- ❌ Don't force push to shared branches
- ❌ Don't merge your own Pull Requests
- ❌ Don't leave branches unmerged for too long

---

## Getting Help

### If You're Stuck

1. **Check this documentation** first
2. **Ask team members** for guidance
3. **Search online** for specific Git commands
4. **Use Git help:** `git help <command>`

### Useful Resources

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf

---

## Summary

### Remember These Key Points

1. **Three branches:** `main` (stable) → `develop` (integration) → `feature/*` (work)
2. **Branch naming:** `feature/short-descriptive-name`
3. **Commit format:** `Prefix: description in lowercase`
4. **Workflow:** Create branch → Code → Commit → Push → PR → Review → Merge
5. **No direct commits** to `main` or `develop`
6. **Only team lead** merges to `main`
7. **Delete branches** after merge
8. **Pull before push** to avoid conflicts

---

**Happy Coding! 🚀**

*For questions about this workflow, contact the team lead or refer to project documentation.*

---

*Last Updated: January 2024*
