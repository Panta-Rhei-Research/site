---
{
  "projection_kind": "taulib_declaration",
  "title": "from_sectors",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/from-sectors/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::from_sectors",
  "declaration_slug": "from-sectors",
  "kind": "def",
  "name": "from_sectors",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 196,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L196-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/verify/taulib/docs/book-i-boundary-split-complex/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L196-L197",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Boundary.SplitComplex](/verify/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L196-L197)
- Source range: L196-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Inverse of to_sectors: recover SplitComplex from SectorPair.
    Given (u, v) = (a+b, a-b), recover a = (u+v)/2, b = (u-v)/2.
    Over integers, this requires u+v and u-v to be even, which is
    always the case since u and v have the same parity. We work
    formally: from_sectors(to_sectors(z)) = z is proved directly. -/
```

## Source Excerpt

```lean
def from_sectors (s : SectorPair) : SplitComplex :=
  ⟨(s.b_sector + s.c_sector) / 2, (s.b_sector - s.c_sector) / 2⟩
```
