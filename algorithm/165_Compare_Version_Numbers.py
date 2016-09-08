class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list_version1 = version1.split(".")
        list_version2 = version2.split(".")

        for i in range(len(list_version1)):
            list_version1[i] = int(list_version1[i])

        for i in range(len(list_version2)):
            list_version2[i] = int(list_version2[i])

        max_length = max(len(list_version1),len(list_version2))
        if len(list_version1) < max_length:
            for i in range(max_length-len(list_version1)):
                list_version1.append(0)

        if len(list_version2) < max_length:
            for i in range(max_length-len(list_version2)):
                list_version2.append(0)

        for i in range(max_length):
            if list_version1[i] > list_version2[i]:
                return 1
            elif list_version1[i] < list_version2[i]:
                return -1
            else:
                # equal
                pass

        # still equal here
        return 0


t = Solution()
print t.compareVersion("1.0.1", "1")
