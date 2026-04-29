---
{
  "projection_kind": "taulib_declaration",
  "title": "NCGSpectralTriple",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/ncgspectral-triple/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::NCGSpectralTriple",
  "declaration_slug": "ncgspectral-triple",
  "kind": "structure",
  "name": "NCGSpectralTriple",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 203,
  "source_line_end": 212,
  "registry_ids": [
    "V.P106"
  ],
  "related_registry_items": [
    {
      "id": "V.P106",
      "title": "NCG spectral triple from tau",
      "url": "/registry/object/V.P106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L203-L212",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L203-L212",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L203-L212)
- Source range: L203-L212
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P106` — NCG spectral triple from tau

## Immediate Comment / Docstring

```lean
/-- [V.P106] NCG spectral triple from tau: the boundary holonomy
    algebra at E1 determines a canonical spectral triple (A, H, D):

    A_tau = O(tau^3) = A_spec(L) (Central Theorem, Book II)
    H_tau = L^2 completion of boundary characters
    D_tau = Dirac operator from boundary holonomy connection

    This spectral triple reproduces the Connes-Lott model for the
    Standard Model at E1 level, but is determined uniquely (no
    choice of finite geometry). -/
```

## Source Excerpt

```lean
structure NCGSpectralTriple where
  /-- Algebra is O(tau^3) = A_spec(L). -/
  algebra_from_central_thm : Bool := true
  /-- Hilbert space from boundary characters. -/
  hilbert_from_characters : Bool := true
  /-- Dirac from holonomy connection. -/
  dirac_from_holonomy : Bool := true
  /-- Triple is uniquely determined (no choice). -/
  uniquely_determined : Bool := true
  deriving Repr
```
