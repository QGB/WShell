@if "%1"=="" (goto curr)
@rem : explorer "C:\Program Files\qBittorrent\"  ·���к��� / �޷���ȷִ�� 
: batҪ�� gb2312���뱣��,����ѡ�� CR LF����Ȼ utf-8ִ�г���

@start "" explorer "%*"
cd "%*"
: ����Ϊ���·��ʱ ��cd�ᵼ�� ��start �Ҳ���·��


@goto end

:curr
@start "" explorer .

:end
