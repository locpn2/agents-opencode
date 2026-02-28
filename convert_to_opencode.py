import os
import re
import shutil
from pathlib import Path

def convert_agent(input_file, output_dir):
    """Convert Claude Code agent to OpenCode format"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]
            
            # Extract name and description
            name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
            model_match = re.search(r'^model:\s*(.+)$', frontmatter, re.MULTILINE)
            
            if name_match:
                agent_name = name_match.group(1).strip()
                
                # Build new frontmatter
                new_frontmatter = ["---"]
                new_frontmatter.append(f"description: {desc_match.group(1).strip() if desc_match else ''}")
                new_frontmatter.append("mode: subagent")
                
                if model_match:
                    model = model_match.group(1).strip()
                    if model != 'inherit':
                        new_frontmatter.append(f"model: anthropic/claude-{model}-4-20250514")
                
                new_frontmatter.append("---")
                
                # Write converted file
                output_file = os.path.join(output_dir, f"{agent_name}.md")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_frontmatter) + body)
                print(f"Converted: {input_file} -> {output_file}")
                return True
    
    return False

def convert_skill(input_file, output_dir):
    """Convert Claude Code skill to OpenCode format"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]
            
            # Extract name
            name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
            
            if name_match:
                skill_name = name_match.group(1).strip()
                
                # Build new frontmatter
                new_frontmatter = ["---"]
                new_frontmatter.append(f"name: {skill_name}")
                
                # Find description and add it
                desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
                if desc_match:
                    new_frontmatter.append(f"description: {desc_match.group(1).strip()}")
                
                # Add compatibility
                new_frontmatter.append("compatibility: opencode")
                new_frontmatter.append("---")
                
                # Create skill directory and file
                skill_dir = os.path.join(output_dir, skill_name)
                os.makedirs(skill_dir, exist_ok=True)
                output_file = os.path.join(skill_dir, "SKILL.md")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_frontmatter) + body)
                print(f"Converted: {input_file} -> {output_file}")
                return True
    
    return False

# Convert agents
agents_input = Path("plugins")
agents_output = ".opencode/agents"

agent_count = 0
for plugin_dir in agents_input.iterdir():
    if plugin_dir.is_dir():
        agents_dir = plugin_dir / "agents"
        if agents_dir.exists():
            for agent_file in agents_dir.glob("*.md"):
                if convert_agent(agent_file, agents_output):
                    agent_count += 1

print(f"\nTotal agents converted: {agent_count}")

# Convert skills
skills_input = Path("plugins")
skills_output_opencode = ".opencode/skills"
skills_output_claude = ".claude/skills"

skill_count = 0
for plugin_dir in skills_input.iterdir():
    if plugin_dir.is_dir():
        skills_dir = plugin_dir / "skills"
        if skills_dir.exists():
            for skill_subdir in skills_dir.iterdir():
                if skill_subdir.is_dir():
                    skill_file = skill_subdir / "SKILL.md"
                    if skill_file.exists():
                        if convert_skill(skill_file, skills_output_claude):
                            skill_count += 1
                        # Also create in .opencode/skills for native support
                        if convert_skill(skill_file, skills_output_opencode):
                            pass

print(f"Total skills converted: {skill_count}")
