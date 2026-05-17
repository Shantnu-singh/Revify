# Claude Context Window Management
## Claude Context Window
- CW : amt of info llm take to understand the user query/
- What is in CW : codebase , specs , jira/github issue , slack/ msg, previous ai chats, githist / PRs
- CW : Model working directly

## Claudecode context window 
- usally 200k
- each session has fresh CW
- token -> Input & Output both get used
- noormally 6x token get send to claude, then your msg
- entire conversation hist get sends to the claude, each time 
- Try to keep conversation small and keep spec per session
- subagents get their own isolated CW 
- subagents return only a summary to main context - so not to full the CW

- Nornally we get 80% of the total Cw space. 20% by system tokens
- Cw : system promts + tools schema + claude.md + coonversation hist + tool results + skills + mcp + auto compaxt (33k reserved)

## what happens when context-window is full
- Stage 1 : Quality Degrades
- Stage 2: Auto - compaction Triggers ( 75-92% full)
- Stage 3: Repeated Compaction Caused Corruption
- Stage 4: Hard Stop

- We can also compress using /compact (compression is not lossless, hence it is good to compact when you feel it)
- Start a subagents for the next task
- /clear or start new session

## Good Practices
- one session per featurs
- use /compact ( proactively, Not Reactively)
- write Focused, spefic promtpt
- Use Subagents for Isolated or Explorary Work
- use .claudeignore to keep irrelavtn files out (New)

# Claude.md file
- Llm doesn;t have memory
- Claude doesn't remeber things form prv session 
- need repeated instraction
- Repeating instraction each time -> hard, inconsistent, and errors

- is a markdown file, like a persisatnt system prompt

## How to Create
- can create Mantually CLAUDE.ms
- using /init
- /init useful in starting, new project and less knowns person