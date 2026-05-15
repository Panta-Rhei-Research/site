---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_check",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/goldbach-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::goldbach_check",
  "declaration_slug": "goldbach-check",
  "kind": "def",
  "name": "goldbach_check",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 82,
  "source_line_end": 91,
  "registry_ids": [
    "III.D95"
  ],
  "related_registry_items": [
    {
      "id": "III.D95",
      "title": "Goldbach Representation",
      "url": "/registry/object/III.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L82-L91",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/corpus/taulib/docs/book-iii-spectral-additive-conjectures/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L82-L91",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/corpus/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L82-L91)
- Source range: L82-L91
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D95` — Goldbach Representation

## Immediate Comment / Docstring

```lean
/-- [III.D95] Goldbach check: all even numbers from 4 to bound have
    a Goldbach representation. -/
```

## Source Excerpt

```lean
def goldbach_check (bound : Nat) : Bool :=
  go 4 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      let ok := n % 2 != 0 || goldbach_pair n
      ok && go (n + 1) (fuel - 1)
  termination_by fuel
```
