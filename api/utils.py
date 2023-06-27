import requests


def get_all_repos(username: str, access_token: str) -> list:
    api_url = 'https://api.github.com'
    response = requests.get(f'{api_url}/users/{username}/repos',
                        headers={'Authorization': f'token {access_token}'})
    if response.status_code == 200:
        repos = [repo['name'] for repo in response.json()]
        return repos
    else:
        print(f'Error: {response.status_code}')


def get_branch_and_tags(owner: str, access_token: str, repo: str):
    api_url = 'https://api.github.com'
    path = f'{api_url}/repos/{owner}/{repo}'
    response = requests.get(
        path,
        headers={'Authorization': f'token {access_token}'}
    )
    branches_response = requests.get(
        f'{path}/branches',
        headers={'Authorization': f'token {access_token}'}
    )
    tags_response = requests.get(
        f'{path}/tags',
        headers={'Authorization': f'token {access_token}'}
    )

    status_code = [response.status_code, branches_response.status_code, tags_response.status_code]

    match status_code:
        case [200, 200, 200]:
            repo_info = response.json()
            name = repo_info['name']
            branches = [branch['name'] for branch in branches_response.json()]
            tags = [tag['name'] for tag in tags_response.json()]
            return name, branches, tags
        case _:
            return status_code
