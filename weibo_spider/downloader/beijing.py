import os
class CoverImageDownloader:
    """下载用户主页背景图"""
    
    def __init__(self, file_dir, timeout):
        self.file_dir = file_dir
        self.timeout = timeout
    
    def download_cover(self, url, user_id):
        """下载背景图并保存"""
        try:
            import requests
            from requests.adapters import HTTPAdapter
            from requests.packages.urllib3.util.retry import Retry
            
            # 设置文件名
            file_name = f'{user_id}_cover.jpg'
            file_path = os.path.join(self.file_dir, file_name)
            
            # 如果文件已存在，跳过
            if os.path.isfile(file_path):
                print(f'背景图已存在: {file_name}')
                return
            
            # 下载图片
            session = requests.Session()
            retry = Retry(total=self.timeout[0], backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            response = session.get(
                url,
                timeout=(self.timeout[1], self.timeout[2])
            )
            
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f'背景图下载成功: {file_name}')
            else:
                print(f'背景图下载失败，状态码: {response.status_code}')
                
        except Exception as e:
            print(f'下载背景图时出错: {e}')