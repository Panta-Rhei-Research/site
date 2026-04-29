---
{
  "projection_kind": "taulib_declaration",
  "title": "cofinal_30",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/cofinal-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::cofinal_30",
  "declaration_slug": "cofinal-30",
  "kind": "theorem",
  "name": "cofinal_30",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 187,
  "source_line_end": 187,
  "registry_ids": [
    "III.T09"
  ],
  "related_registry_items": [
    {
      "id": "III.T09",
      "title": "Primorial Cofinality",
      "url": "/registry/object/III.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L187-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.PrimorialLadder",
        "url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L187-L187",
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

- Module: [TauLib.BookIII.Spectral.PrimorialLadder](/verify/taulib/docs/book-iii-spectral-primorial-ladder/)
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L187-L187)
- Source range: L187-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T09` — Primorial Cofinality

## Immediate Comment / Docstring

```lean
/-- [III.T09] Structural: cofinal level of 30 is 3. -/
```

## Source Excerpt

```lean
theorem cofinal_30 : cofinal_level 30 = 3 := by native_decide
```
