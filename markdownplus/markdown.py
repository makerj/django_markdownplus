"""
The MIT License (MIT)

Copyright (c) 2016 Junhui Lee <ohenwkgdj@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import markdown as markdown2
from bleach import clean
from markdown.inlinepatterns import Pattern
from markdown.util import etree
from markdown.extensions import Extension


class AudioTagPattern(Pattern):
    PATTERN = r'!a\[(.*)\]\(([^ ]*)( .*)?\)'

    @classmethod
    def new_instance(cls):
        return cls(cls.PATTERN)

    def handleMatch(self, m):
        alt, src, title = m.group(2), m.group(3), m.group(4)
        elem = etree.Element('audio')
        elem.set('controls', '')
        elem.set('alt', alt or '')
        elem.set('src', src or '')
        elem.set('title', title or '')
        return elem


class VideoTagPattern(Pattern):
    PATTERN = r'!v\[(.*)\]\(([^ ]*)( .*)?\)'

    @classmethod
    def new_instance(cls):
        return cls(cls.PATTERN)

    def handleMatch(self, m):
        alt, src, title = m.group(2), m.group(3), m.group(4)
        elem = etree.Element('video')
        elem.set('controls', '')
        elem.set('alt', alt or '')
        elem.set('src', src or '')
        elem.set('title', title or '')
        return elem


class MediaExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('audiotagpattern', AudioTagPattern.new_instance(), '_begin')
        md.inlinePatterns.add('videotagpattern', VideoTagPattern.new_instance(), '_begin')


def markdown(text):
    return markdown2.markdown(clean(text), extensions=[MediaExtension(), ])
