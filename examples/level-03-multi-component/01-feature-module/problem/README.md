# Problem: Feature Module Without Shared Types

This example demonstrates a feature that spans frontend and backend but has no shared type definitions, causing inconsistencies and making it difficult for AI to coordinate changes.

## The Problem

Without shared types, AI struggles because:

1. **Type mismatches**: Frontend and backend define types separately
2. **Inconsistencies**: Changes to one side don't propagate to the other
3. **Coordination difficulty**: AI can't verify types match across components
4. **Validation gaps**: Different validation rules on frontend vs backend

## Run the Code

```bash
# Backend
cd backend
pip install flask
python main.py

# Frontend (in another terminal)
cd frontend
npm install
npm start
```

## Issues to Notice

- Backend uses `age` as required, frontend as optional
- No shared type definitions
- AI can't verify type consistency
- Changes require manual coordination

