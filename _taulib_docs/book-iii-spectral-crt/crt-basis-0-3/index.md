---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_basis_0_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/crt-basis-0-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::crt_basis_0_3",
  "declaration_slug": "crt-basis-0-3",
  "kind": "theorem",
  "name": "crt_basis_0_3",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 254,
  "source_line_end": 257,
  "registry_ids": [
    "III.P05"
  ],
  "related_registry_items": [
    {
      "id": "III.P05",
      "title": "Independence of Prime-Level Actions",
      "url": "/registry/object/III.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L254-L257",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/verify/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L254-L257",
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

- Module: [TauLib.BookIII.Spectral.CRT](/verify/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L254-L257)
- Source range: L254-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P05` — Independence of Prime-Level Actions

## Immediate Comment / Docstring

```lean
/-- [III.P05] Structural: CRT basis element 0 at depth 3
    has residue 1 mod 2, 0 mod 3, 0 mod 5. -/
```

## Source Excerpt

```lean
theorem crt_basis_0_3 :
    crt_decompose (crt_basis 3 0) 3 = [1, 0, 0] := by native_decide

end Tau.BookIII.Spectral
```
