import json
import os
import subprocess


def run_git_command1(args, cwd=None):
	cmd = ['git'] + args
	print(f'command = {cmd}')
	print(f'cwd = {cwd}')
	if cwd and not os.path.exists(cwd):
		print(f"Directory does not exist: {cwd}")
		return
	print("Directory exists", cwd)
	print("Calling subprocess")
	result = None
	try:
		result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
	except Exception as e:
		print('result= {0}'.format(result))
		print("exception : ", e)
		raise e



def run_git_command(args, cwd=None):
	cmd = ['git'] + args
	print(f'command = {cmd}')
	print(f'cwd = {cwd}')
	if cwd and not os.path.exists(cwd):
		print(f"Directory does not exist: {cwd}")
		return
	result = subprocess.run( cmd, shell=True, cwd=cwd, capture_output=True, text=True)
	if result.returncode != 0:
		print(f"Error running {' '.join(args)}: {result.stderr}")
		raise Exception(result.stderr)
	return result.stdout.strip()

def clone_and_tag_repo(repo_url, branch, tag):
	repo_name = repo_url.rstrip('.git ').split('/')[-1]
	print(f'repo_name = {repo_name}')
	if not os.path.exists(repo_name):
		print(f"Cloning {repo_url}...")
		run_git_command(['clone', repo_url])
	repo_path = os.path.abspath(repo_name)
	print(f"Checking out branch {branch} in {repo_name}...")
	run_git_command(['fetch'], cwd=repo_path)
	run_git_command(['checkout', branch], cwd=repo_path)
	print(f"Creating tag {tag}...")
	run_git_command(['tag', tag], cwd=repo_path)
	print(f"Pushing tag {tag} to remote...")
	run_git_command(['push', 'origin', tag], cwd=repo_path)

def main():
	with open('repo-list.json', 'r') as f:
		repos = json.load(f)
		print(f"Loaded {len(repos)} repositories from repo-list.json")
		print(f"repos = {repos}")
	for repo in repos['repositories']:
		url = repo['url']
		branch = repo['branch']
		tag = repo['tag']
		try:
			clone_and_tag_repo(url, branch, tag)
		except Exception as e:
			print(f"Failed to process {url}: {e}")

if __name__ == "__main__":
	main()

