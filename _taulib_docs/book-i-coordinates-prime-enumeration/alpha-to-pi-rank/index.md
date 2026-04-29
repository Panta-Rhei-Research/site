---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_to_pi_rank",
  "permalink": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/alpha-to-pi-rank/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::alpha_to_pi_rank",
  "declaration_slug": "alpha-to-pi-rank",
  "kind": "def",
  "name": "alpha_to_pi_rank",
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 105,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L105-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L105-L105",
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/verify/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L105-L105)
- Source range: L105-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The reverse projection: for prime p, its π-rank. -/
```

## Source Excerpt

```lean
def alpha_to_pi_rank (p : TauIdx) : TauIdx := prime_index p
```
