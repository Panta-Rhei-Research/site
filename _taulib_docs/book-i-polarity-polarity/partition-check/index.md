---
{
  "projection_kind": "taulib_declaration",
  "title": "partition_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarity/partition-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Polarity`.",
  "declaration_id": "TauLib.BookI.Polarity.Polarity::partition_check",
  "declaration_slug": "partition-check",
  "kind": "def",
  "name": "partition_check",
  "module_name": "TauLib.BookI.Polarity.Polarity",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarity/",
  "source_line_start": 220,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L220-L221",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Polarity",
        "url": "/verify/taulib/docs/book-i-polarity-polarity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L220-L221",
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

- Module: [TauLib.BookI.Polarity.Polarity](/verify/taulib/docs/book-i-polarity-polarity/)
- Source path: [`TauLib/BookI/Polarity/Polarity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L220-L221)
- Source range: L220-L221
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verify that every prime from 2 to n is classified at bound N
    (B-dominant count + C-dominant count = total prime count). -/
```

## Source Excerpt

```lean
def partition_check (n N : TauIdx) : Bool :=
  count_b_dominant n N + count_c_dominant n N == count_primes n
```
