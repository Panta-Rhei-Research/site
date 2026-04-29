---
{
  "projection_kind": "taulib_declaration",
  "title": "characteristic_morphism",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-topos/characteristic-morphism/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::characteristic_morphism",
  "declaration_slug": "characteristic-morphism",
  "kind": "def",
  "name": "characteristic_morphism",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 82,
  "source_line_end": 84,
  "registry_ids": [
    "I.D58"
  ],
  "related_registry_items": [
    {
      "id": "I.D58",
      "title": "Characteristic Morphism",
      "url": "/registry/object/I.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L82-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/verify/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L82-L84",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/verify/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L82-L84)
- Source range: L82-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D58` — Characteristic Morphism

## Immediate Comment / Docstring

```lean
/-- [I.D58] The characteristic morphism: for a given predicate on TauIdx,
    assigns a Truth4 value to each element based on its membership status.

    The predicate P encodes membership; the Truth4 value encodes HOW
    the element is a member (from which spectral sectors). -/
```

## Source Excerpt

```lean
def characteristic_morphism (b_member c_member : TauIdx → Bool) :
    TauIdx → Omega_tau :=
  fun x => Truth4.fromBoolPair (b_member x, c_member x)
```
