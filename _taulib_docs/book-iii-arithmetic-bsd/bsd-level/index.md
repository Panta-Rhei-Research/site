---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_level",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-bsd/bsd-level/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.BSD`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.BSD::bsd_level",
  "declaration_slug": "bsd-level",
  "kind": "theorem",
  "name": "bsd_level",
  "module_name": "TauLib.BookIII.Arithmetic.BSD",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-bsd/",
  "source_line_start": 149,
  "source_line_end": 149,
  "registry_ids": [
    "III.P27"
  ],
  "related_registry_items": [
    {
      "id": "III.P27",
      "title": "BSD Three-Ingredient Proof",
      "url": "/registry/object/III.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L149-L149",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.BSD",
        "url": "/verify/taulib/docs/book-iii-arithmetic-bsd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L149-L149",
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

- Module: [TauLib.BookIII.Arithmetic.BSD](/verify/taulib/docs/book-iii-arithmetic-bsd/)
- Source path: [`TauLib/BookIII/Arithmetic/BSD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L149-L149)
- Source range: L149-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P27` — BSD Three-Ingredient Proof

## Immediate Comment / Docstring

```lean
/-- [III.P27] Structural: BSD is at E₁→E₂ interface. -/
```

## Source Excerpt

```lean
theorem bsd_level : problem_level .BSD = .E2 := rfl
```
