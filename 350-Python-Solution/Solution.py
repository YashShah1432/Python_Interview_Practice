class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        for i in range (0, len(nums1)):
            for j in range (0, len(nums2)):
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    nums2.remove(nums2[j])
                    break
        return result