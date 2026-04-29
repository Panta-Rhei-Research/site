---
{
  "projection_kind": "taulib_declaration",
  "title": "template_invariance_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/template-invariance-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::template_invariance_check",
  "declaration_slug": "template-invariance-check",
  "kind": "def",
  "name": "template_invariance_check",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 83,
  "source_line_end": 99,
  "registry_ids": [
    "III.T06"
  ],
  "related_registry_items": [
    {
      "id": "III.T06",
      "title": "Template Invariance Under Reflection",
      "url": "/registry/object/III.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L83-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L83-L99",
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

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L83-L99)
- Source range: L83-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T06` — Template Invariance Under Reflection

## Immediate Comment / Docstring

```lean
/-- [III.T06] Template invariance check: the four-component layer template
    is preserved under the Langlands₁ reflection.
    The enrichment functor maps E₀ template to compatible E₁ template. -/
```

## Source Excerpt

```lean
def template_invariance_check (bound db : TauIdx) : Bool :=
  let e0 := layer_of .E0 bound db
  let e1 := layer_of .E1 bound db
  go e0 e1 0 1 ((bound + 1) * (db + 1))
where
  go (e0 e1 : LayerTemplate) (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go e0 e1 (x + 1) 1 (fuel - 1)
    else
      -- Template flow: E₀ invariant → E₁ carrier compatibility
      let flow_ok := if e0.invariant_check x k then
        let decoded := e0.decoder x k
        e1.carrier_check decoded k || k == 0
      else true
      flow_ok && go e0 e1 x (k + 1) (fuel - 1)
  termination_by fuel
```
