---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_nonneg_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/bsd-nonneg-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::bsd_nonneg_1",
  "declaration_slug": "bsd-nonneg-1",
  "kind": "theorem",
  "name": "bsd_nonneg_1",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 179,
  "source_line_end": 180,
  "registry_ids": [
    "III.D62"
  ],
  "related_registry_items": [
    {
      "id": "III.D62",
      "title": "BSD Functional",
      "url": "/registry/object/III.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L179-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L179-L180",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L179-L180)
- Source range: L179-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D62` — BSD Functional

## Immediate Comment / Docstring

```lean
/-- [III.D62] Structural: BSD at depth 1 is non-negative. -/
```

## Source Excerpt

```lean
theorem bsd_nonneg_1 :
    bsd_functional 1 ≥ 0 := Nat.zero_le _
```
